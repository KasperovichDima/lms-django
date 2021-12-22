from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

import teachers.forms as forms

from .forms import TeachersFilter
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
        form = forms.TeachersCreateForm()

    elif request.method == 'POST':
        form = forms.TeachersCreateForm(data=request.POST)

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
        form = forms.TeachersUpdateForm(instance=teacher)

    elif request.method == 'POST':
        form = forms.TeachersUpdateForm(data=request.POST, instance=teacher)
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
