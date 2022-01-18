import django.views.generic as CBV
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import groups.forms as forms

from students.models import Student

from .forms import GroupsFilter
from .models import Group


class GroupUpdateView(LoginRequiredMixin, CBV.UpdateView):
    model = Group
    form_class = forms.GroupUpdateForm
    success_url = reverse_lazy('groups:get')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['students'] = self.get_object().students.prefetch_related('headman_in_group')
        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['hdmn'] = self.object.headman.id
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headman = Student.objects.get(id=form.cleaned_data['hdmn'])
        except ValueError:
            pass
        form.instance.save()
        return response


class GroupListView(CBV.ListView):
    model = Group
    template_name = 'groups/list.html'

    def get_queryset(self):
        filter_groups = GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().prefetch_related('students', 'course')
        )
        return filter_groups


class GroupCreateView(LoginRequiredMixin, CBV.CreateView):
    model = Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups:get')
    template_name = 'groups/create.html'


class GroupDeleteView(LoginRequiredMixin, CBV.DeleteView):
    model = Group
    success_url = reverse_lazy('groups:get')

# def create_group(request):
#     if request.method == 'GET':
#         form = forms.GroupCreateForm()
#
#     elif request.method == 'POST':
#         form = forms.GroupCreateForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:get'))
#
#     return render(
#         request=request,
#         template_name='groups/create.html',
#         context={'form': form}
#     )


# def update_group(request, pk):
#     group = Group.objects.get(id=pk)
#     if request.method == 'GET':
#         form = forms.GroupsUpdateForm(instance=group)
#
#     elif request.method == 'POST':
#         form = forms.GroupsUpdateForm(data=request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:get'))
#
#     return render(
#         request=request,
#         template_name='groups/update.html',
#         context={'form': form,
#                  'group': group,
#                  'students': group.students.prefetch_related('headman_in_group'),
#                  }
#     )


# def del_group(request, pk):
#     group = get_object_or_404(Group, id=pk)
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('groups:get'))
#
#     return render(request, 'groups/group_confirm_delete.html', {'group': group})

# def get_groups(request):
#     groups = Group.objects.all().prefetch_related('students', 'course')
#     filter_groups = GroupsFilter(data=request.GET, queryset=groups)
#
#     return render(
#         request,
#         'groups/list.html',
#         {'filter_groups': filter_groups})

# View for handmade form
# def get_groups(request, args):
#     res = Group.objects.all()
#
#     for key, value in args.items():
#         if value:
#             res = res.filter(**{key: value})
#
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={'groups': res}
#     )
