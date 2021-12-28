from django.urls import path

import teachers.views as t_v

app_name = 'teachers'

urlpatterns = [
    path('', t_v.TeacherListView.as_view(), name='get'),
    path('create/', t_v.TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', t_v.TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', t_v.TeacherDeleteView.as_view(), name='delete'),
]
