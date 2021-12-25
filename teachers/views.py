import django.views.generic as CBV
from django.urls import reverse_lazy

import teachers.forms as forms

from .forms import TeachersFilter
from .models import Teacher


class TeacherUpdateView(CBV.UpdateView):
    model = Teacher
    form_class = forms.TeachersUpdateForm
    success_url = reverse_lazy('teachers:get')
    template_name = 'teachers/update.html'


class TeacherDeleteView(CBV.DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:get')


class TeacherCreateView(CBV.CreateView):
    model = Teacher
    form_class = forms.TeachersCreateForm
    success_url = reverse_lazy('teachers:get')
    template_name = 'teachers/create.html'


class TeacherListView(CBV.ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        filter_teachers = TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )
        return filter_teachers


# def get_teachers(request):
#     res = Teacher.objects.all()
#     filter_teachers = TeachersFilter(data=request.GET, queryset=res)
#
#     return render(
#         request,
#         'teachers/list.html',
#         {'filter_teachers': filter_teachers}
#     )


# def create_teacher(request):
#     if request.method == 'GET':
#         form = forms.TeachersCreateForm()
#
#     elif request.method == 'POST':
#         form = forms.TeachersCreateForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={'form': form}
#     )


# def update_teacher(request, pk):
#     teacher = Teacher.objects.get(id=pk)
#     if request.method == 'GET':
#         form = forms.TeachersUpdateForm(instance=teacher)
#
#     elif request.method == 'POST':
#         form = forms.TeachersUpdateForm(data=request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(
#         request=request,
#         template_name='teachers/update.html',
#         context={'form': form}
#     )


# def del_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(request, 'teachers/group_confirm_delete.html', {'teacher': teacher})

# def get_teachers(request):
#     res = Teacher.objects.all()
#     filter_teachers = TeachersFilter(data=request.GET, queryset=res)
#
#     return render(
#         request,
#         'teachers/list.html',
#         {'filter_teachers': filter_teachers}
#     )


# def create_teacher(request):
#     if request.method == 'GET':
#         form = forms.TeachersCreateForm()
#
#     elif request.method == 'POST':
#         form = forms.TeachersCreateForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={'form': form}
#     )


# def update_teacher(request, pk):
#     teacher = Teacher.objects.get(id=pk)
#     if request.method == 'GET':
#         form = forms.TeachersUpdateForm(instance=teacher)
#
#     elif request.method == 'POST':
#         form = forms.TeachersUpdateForm(data=request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(
#         request=request,
#         template_name='teachers/update.html',
#         context={'form': form}
#     )


# def del_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:get'))
#
#     return render(request, 'teachers/group_confirm_delete.html', {'teacher': teacher})
