from django.urls import path

import students.views as st_v

app_name = 'students'

urlpatterns = [
    path('', st_v.get_students, name='get'),
    path('create/', st_v.create_student, name='create'),
    path('update/<int:pk>/', st_v.update_student, name='update'),
    path('delete/<int:pk>/', st_v.del_student, name='delete'),
    path('generate_students/', st_v.gen_std,  name='generate'),
]
