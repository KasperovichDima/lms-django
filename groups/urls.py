from django.urls import path

import groups.views as g_v

app_name = 'groups'

urlpatterns = [
    path('', g_v.GroupListView.as_view(), name='get'),
    path('create/', g_v.GroupCreateView.as_view(), name='create'),
    path('update/<int:pk>/', g_v.GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', g_v.GroupDeleteView.as_view(), name='delete'),
]
