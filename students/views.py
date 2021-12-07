from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webargs.djangoparser import use_args

from .forms import StudentCreateForm
from .models import Student

from webargs import fields, validate    # noqa

from .utils import qset_to_html


def index(request):
    return HttpResponse('<h1>Django LMS Project</h1>')

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
        context={'students':res}
    )


# @csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()

    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    # html_form = f"""
    #     <form method="post">
    #     {form.as_p()}
    #     <input type="submit" value="Create">
    #     </form>
    # """
    #
    # return HttpResponse(html_form)

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)

    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST,
                                 instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    html_form = f"""
        <form method="post">
        {form.as_p()}
        <input type="submit" value="Update">
        </form>
    """

    return HttpResponse(html_form)