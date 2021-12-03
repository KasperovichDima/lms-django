"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.contrib import admin
from django.urls import path, re_path, include   # # noqa

import groups.views as g_v

import students.views as st_v

import teachers.views as t_v


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('generate_students/', st_v.gen_std),
    path('students/', st_v.get_students, name='get_students'),
    path('groups/', g_v.get_groups, name='get_groups'),
    path('teachers/', t_v.get_teachers, name='get_teachers'),
    path('students/create/', st_v.create_student, name='create_student'),
    path('groups/create/', g_v.create_group, name='create_group'),
    path('teachers/create/', t_v.create_teacher, name='create_teacher'),

]
