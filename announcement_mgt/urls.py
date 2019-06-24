from django.contrib import admin
from django.urls import path, include
from .views import AnnouncementListView, AnnouncementDetailView, AnnouncementCreateView, AnnouncementEditView, AnnouncementDeleteView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name="post_list"),
    path('view/<int:pk>/',AnnouncementDetailView.as_view(), name='post_detail'),
    path('new/',AnnouncementCreateView.as_view(), name='post_new'),
    path('edit/<int:pk>',AnnouncementEditView.as_view(), name='post_edit'),
    path('del/<int:pk>',AnnouncementDeleteView.as_view(), name='post_delete'),
]
