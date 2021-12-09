from django.http import HttpResponseRedirect
from django.shortcuts import render   # noqa

from webargs import fields, validate    # noqa
from webargs.djangoparser import use_args

from .forms import GroupsCreateForm
from .models import Group


@use_args(
    {
        'course_name': fields.Str(required=False),
        'start_date': fields.Date(required=False),
        'number_of_students': fields.Int(required=False),
        'teacher_name': fields.Str(required=False)
    },
    location='query'
)
def get_groups(request, args):
    res = Group.objects.all()
    form = GroupsCreateForm()

    for key, value in args.items():
        if value:
            res = res.filter(**{key: value})

    # return render(
    #     request=request,
    #     template_name='groups/list.html',
    #     context={'groups': res, 'form': form}

    return render(
        request,
        'groups/list.html',
        {'groups': res, 'form': form}
    )


def create_group(request):
    if request.method == 'GET':
        form = GroupsCreateForm()

    elif request.method == 'POST':
        form = GroupsCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupsCreateForm(instance=group)

    elif request.method == 'POST':
        form = GroupsCreateForm(data=request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )


# Вью для формы, написанной вручную
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
