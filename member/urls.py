from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('members/', views.memberListView.as_view()),
    path('members/<str:pk>/', views.memberDetails.as_view()),
    path('membersbyantenne/<str:pk>/', views.memberByAntenneDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
