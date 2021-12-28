import django.views.generic as CBV
from django.shortcuts import render
from django.urls import reverse_lazy

import students.forms as forms

from .forms import StudentsFilter
from .models import Student


def gen_std(request):
    return render(
        request=request,
        template_name='students/generate.html',
        context={'result': Student.generate_students(request)}
    )


class StudentUpdateView(CBV.UpdateView):
    model = Student
    form_class = forms.StudentUpdateForm
    success_url = reverse_lazy('students:get')
    template_name = 'students/update.html'


class StudentCreateView(CBV.CreateView):
    model = Student
    form_class = forms.StudentCreateForm
    success_url = reverse_lazy('students:get')
    template_name = 'students/create.html'


class StudentDeleteView(CBV.DeleteView):
    model = Student
    success_url = reverse_lazy('students:get')


class StudentListView(CBV.ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        filter_students = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_in_group')
        )
        return filter_students

# def create_student(request):
#     if request.method == 'GET':
#         form = forms.StudentCreateForm()
#
#     elif request.method == 'POST':
#         form = forms.StudentCreateForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:get'))
#
#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={'form': form}
#     )


# def update_student(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == 'GET':
#         form = forms.StudentUpdateForm(instance=student)
#
#     elif request.method == 'POST':
#         form = forms.StudentUpdateForm(data=request.POST,
#                                        instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:get'))
#
#     return render(
#         request=request,
#         template_name='students/update.html',
#         context={'form': form}
#     )


# def del_student(request, pk):
#     student = get_object_or_404(Student, id=pk)
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:get'))
#
#     return render(request, 'students/group_confirm_delete.html', {'student': student})


# def get_students(request):
#
#     res = Student.objects.all().select_related('group', 'headman_in_group')
#     filter_students = StudentsFilter(
#         data=request.GET,
#         queryset=res
#         )
#
#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={'filter_students': filter_students},
#     )
