from django.urls import path

from main.views import *

urlpatterns = [
    path('all/', PublicationsListCreateView.as_view(), name='publication-list'),
    path('detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail')
]
