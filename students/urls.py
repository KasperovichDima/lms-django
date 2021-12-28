from django.urls import path

import students.views as st_v

app_name = 'students'

urlpatterns = [
    path('', st_v.StudentListView.as_view(), name='get'),
    path('create/', st_v.StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', st_v.StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', st_v.StudentDeleteView.as_view(), name='delete'),
    path('generate_students/', st_v.gen_std,  name='generate'),
]
