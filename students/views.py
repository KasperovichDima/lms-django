from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from webargs.djangoparser import use_args

from .forms import StudentCreateForm
from .models import Student

from webargs import fields, validate    # noqa


def index(request):

    return render(
        request=request,
        template_name='students/homepage.html',
        context={'greetings': 'Django LMS Project'}
    )


def gen_std(request):
    return HttpResponse(Student.generate_students(request))


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False)
    },
    location='query'
)
def get_students(request, args):
    res = Student.objects.all()
    if args:
        for k, v in args.items():
            res = res.filter(**{k: v})

    return render(
        request=request,
        template_name='students/list.html',
        context={'students': res}
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()

    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)

    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST,
                                 instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )
