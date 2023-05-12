from django.urls import path
from cages import views

app_name = 'cages'
urlpatterns = [
    path("", views.CageListView.as_view(), name="list"),
    path("cage/<int:pk>/", views.CageDetailView.as_view(), name="detail"),
    path("create/", views.CageCreateView.as_view(), name="create"),
]
