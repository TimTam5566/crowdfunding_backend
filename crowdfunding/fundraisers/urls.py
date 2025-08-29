from django.urls import path
from . import views
urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()), # returns a list of all fundraisers
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),  # returns a specific fundraiser
    path('pledges/', views.PledgeList.as_view()), # returns a list of all pledges
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()) # returns a specific pledge
    ] 