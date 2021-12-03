from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render   # noqa
from django.views.decorators.csrf import csrf_exempt

from students.utils import qset_to_html

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

    html_form = """
            <form method="get">
                <label for="fname">First Name:</label>
                <input type="text" id="fname" name="first_name"></br></br>

                <label for="lname">Last Name:</label>
                <input type="text" id="lname" name="last_name"></br></br>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age"></br></br>

                <label for="spec">Specialization:</label>
                <input type="text" id="spec" name="specialization"></br></br>

                <label for="wex">Work Experience:</label>
                <input type="number" id="wex" name="work_experience"></br></br>

                <input type="submit" value="Submit">
            </form>
        """

    return HttpResponse(html_form + qset_to_html(res))


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeachersCreateForm()

    elif request.method == 'POST':
        form = TeachersCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    html_form = f"""
           <form method="post">
           {form.as_p()}
           <input type="submit" value="Submit">
           </form>
       """

    return HttpResponse(html_form)
