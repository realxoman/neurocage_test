from django.urls import path
from cages import views

urlpatterns = [
    path("", views.CageListView.as_view(), name="cages_list"),
    path("cage/<int:pk>/", views.CageListView.as_view(), name="cages_list"),
    path("create/", views.CageListView.as_view(), name="cages_list"),
]
