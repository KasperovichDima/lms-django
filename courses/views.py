import courses.forms as forms

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Course


def get_courses(request):
    courses = Course.objects.all().select_related('group')
    filter_courses = forms.CoursesFilter(data=request.GET, queryset=courses)

    return render(
        request,
        'courses/list.html',
        {'filter_courses': filter_courses})


def create_course(request):
    if request.method == 'GET':
        form = forms.CourseCreateForm()

    elif request.method == 'POST':
        form = forms.CourseCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:get'))

    return render(request, 'courses/create.html', {'form': form})


def update_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.CourseUpdateForm(instance=course)

    elif request.method == 'POST':
        form = forms.CourseUpdateForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:get'))

    return render(request, 'courses/update.html', {'form': form})


def del_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:get'))

    return render(request, 'courses/del.html', {'course': course})
