from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .forms import TeachersFilter
from .forms import TeachersForm
from .models import Teacher

from webargs import fields, validate    # noqa


def get_teachers(request):
    res = Teacher.objects.all()
    filter_teachers = TeachersFilter(data=request.GET, queryset=res)

    return render(
        request,
        'teachers/list.html',
        {'filter_teachers': filter_teachers}
    )


def create_teacher(request):
    if request.method == 'GET':
        form = TeachersForm()

    elif request.method == 'POST':
        form = TeachersForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:get'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


def update_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'GET':
        form = TeachersForm(instance=teacher)

    elif request.method == 'POST':
        form = TeachersForm(data=request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:get'))

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )


def del_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:get'))

    return render(request, 'teachers/del.html', {'teacher': teacher})
