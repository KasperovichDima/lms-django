from django.urls import path

import teachers.views as t_v

app_name = 'teachers'

urlpatterns = [
    path('', t_v.get_teachers, name='get'),
    path('create/', t_v.create_teacher, name='create'),
    path('update/<int:pk>/', t_v.update_teacher, name='update'),
    path('delete/<int:pk>/', t_v.del_teacher, name='delete'),
]
