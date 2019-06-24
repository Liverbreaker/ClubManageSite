from django.contrib import admin
from django.urls import path, include
# from .views import ActivityListView, ActivityCreateView
from .views import (ActivityListView, ActivityDetailView, ActivityCreateView,
                    ActivityEditView, ActivityComfirmCloseView, ActivityComfirmDeleteView,
                    )
#                     ActivitySignupView, ActivitySignedListView, ActivitySignedEditView,
#                     ActivitySignedDeleteView, ActivitySignedDetailView, ActivitySignedAllListView,
#                     ActivitySignedAllDeleteView)

urlpatterns = [
    path('', ActivityListView.as_view(), name="activity-list"),
    path('view/<int:pk>', ActivityDetailView.as_view(), name="activity-detail"),
    path('new/', ActivityCreateView.as_view(), name="activity-create"),
    path('edit/<int:pk>', ActivityEditView.as_view(), name="activity-edit"),
    path('close/<int:pk>', ActivityComfirmCloseView.as_view(), name="activity-close"),
    path('del/<int:pk>', ActivityComfirmDeleteView.as_view(), name="activity-delete"),
    # path('', ActivitySignupView.as_view(), name="activity-signup"),
    # path('', ActivitySignedListView.as_view(), name="activity-signed-list"),
    # path('', ActivitySignedDetailView.as_view(), name="activity-signed-detail"),
    # path('', ActivitySignedEditView.as_view(), name="activity-signed-edit"),
    # path('', ActivitySignedDeleteView.as_view(), name="activity-signed-delete"),
    # path('', ActivitySignedAllListView.as_view(), name="activity-signed-all-list"),
    # path('', ActivitySignedAllDeleteView.as_view(), name="activity-signed-all-delete"),
]
