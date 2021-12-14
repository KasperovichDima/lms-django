from django.urls import path

import groups.views as g_v

app_name = 'groups'

urlpatterns = [
    path('', g_v.get_groups, name='get'),
    path('create/', g_v.create_group, name='create'),
    path('update/<int:pk>/', g_v.update_group, name='update'),
    path('delete/<int:pk>/', g_v.del_group, name='delete'),
]
