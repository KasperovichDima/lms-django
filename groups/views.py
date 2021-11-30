from django.shortcuts import render   # noqa
from django.http import HttpResponse   # noqa

from students.utils import qset_to_html

from webargs import fields, validate    # noqa
from webargs.djangoparser import use_args

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

    for key, value in args.items():
        if value:
            res = res.filter(**{key: value})

    html_form = """
        <form method="get">
            <label for="cname">Course:</label>
            <input type="text" id="cname" name="course_name"></br></br>

            <label for="sdate">Start Date:</label>
            <input type="date" id="sdate" name="start_date"></br></br>

            <label for="nfs">Number of Students:</label>
            <input type="number" id="nfs" name="number_of_students"></br></br>

            <label for="tname">Teacher Name:</label>
            <input type="text" id="tname" name="teacher_name"></br></br>

            <input type="submit" value="Submit">
        </form>
    """

    return HttpResponse(html_form + qset_to_html(res))
