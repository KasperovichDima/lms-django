from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

import groups.forms as forms

from .forms import GroupsFilter
from .models import Group


def get_groups(request):
    res = Group.objects.all().prefetch_related('students')
    filter_groups = GroupsFilter(data=request.GET, queryset=res)

    return render(
        request,
        'groups/list.html',
        {'filter_groups': filter_groups})


def create_group(request):
    if request.method == 'GET':
        form = forms.GroupsCreateForm()

    elif request.method == 'POST':
        form = forms.GroupsCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:get'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.GroupsUpdateForm(instance=group)

    elif request.method == 'POST':
        form = forms.GroupsUpdateForm(data=request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:get'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form,
                 'group': group,
                 'students': group.students.prefetch_related('headman_in_group'),
                 }
    )


def del_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:get'))

    return render(request, 'groups/del.html', {'group': group})

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
