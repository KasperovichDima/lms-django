from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


from .forms import StudentForm
from .forms import StudentsFilter
from .models import Student

from webargs import fields, validate    # noqa


def gen_std(request):
    # return HttpResponse(Student.generate_students(request))
    return render(
        request=request,
        template_name='students/generate.html',
        context={'result': Student.generate_students(request)}
    )


def get_students(request):

    res = Student.objects.all().select_related('group', 'headman_in_group')
    filter_students = StudentsFilter(data=request.GET, queryset=res)

    return render(
        request=request,
        template_name='students/list.html',
        context={'filter_students': filter_students},
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentForm()

    elif request.method == 'POST':
        form = StudentForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:get'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)

    elif request.method == 'POST':
        form = StudentForm(data=request.POST,
                           instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:get'))

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )


def del_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:get'))

    return render(request, 'students/del.html', {'student': student})
