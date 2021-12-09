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
from django.urls import include
from django.urls import path

import groups.views as g_v

import students.views as st_v

import teachers.views as t_v


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', st_v.index, name='index'),
    # Students
    path('students/', include('students.urls')),
    # Groups
    path('groups/', g_v.get_groups, name='get_groups'),
    path('groups/create/', g_v.create_group, name='create_group'),
    path('groups/update/<int:pk>/', g_v.update_group, name='update_group'),
    # Teachers
    path('teachers/', t_v.get_teachers, name='get_teachers'),
    path('teachers/create/', t_v.create_teacher, name='create_teacher'),
    path('teachers/update/<int:pk>/', t_v.update_teacher, name='update_teacher'),
]
