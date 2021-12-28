import courses.views as c_v

from django.urls import path


app_name = 'courses'

urlpatterns = [
    path('', c_v.get_courses, name='get'),
    path('create/', c_v.create_course, name='create'),
    path('update/<int:pk>/', c_v.update_course, name='update'),
    path('delete/<int:pk>/', c_v.del_course, name='delete'),
]
