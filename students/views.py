from django.http import HttpResponse
from django.shortcuts import render # noqa

from webargs.djangoparser import use_args

from .models import Student

from webargs import fields, validate    # noqa

from .utils import qset_to_html


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

    html_form = """
            <form method="get">
                <label for="fname">First name:</label>
                <input type="text" id="fname" name="first_name"></br></br>

                <label for="lname">Last name:</label>
                <input type="text" id="lname" name="last_name"></br></br>

                <label for="age">Age:</label>
                <input type="number" name="age"></br></br>

                <input type="submit" value="Submit">
            </form>
        """

    return HttpResponse(html_form + qset_to_html(res))
