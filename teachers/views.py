from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TeachersCreateForm
from .models import Teacher

from webargs import fields, validate    # noqa
from webargs.djangoparser import use_args


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False),
        'specialization': fields.Str(required=False),
        'work_experience': fields.Int(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    res = Teacher.objects.all()

    for key, value in args.items():
        if value:
            res = res.filter(**{key: value})

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'teachers': res}
    )


def create_teacher(request):
    if request.method == 'GET':
        form = TeachersCreateForm()

    elif request.method == 'POST':
        form = TeachersCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


def update_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'GET':
        form = TeachersCreateForm(instance=teacher)

    elif request.method == 'POST':
        form = TeachersCreateForm(data=request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )
