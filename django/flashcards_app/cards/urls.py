from django.urls import path

from . import views

urlpatterns = [
    path("", views.CardListView.as_view(), name="card-list"),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("stage/<int:stage_num>", views.StageView.as_view(), name="stage"),
]
