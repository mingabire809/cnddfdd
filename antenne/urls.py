from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('antennes/', views.antenneListView.as_view()),
    path('antennes/<int:pk>/', views.antenneDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
