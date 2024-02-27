from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('', views.list_view, name="articles"),
    path('create/', views.create_view, name="create"),
    path('<int:id>/', views.detail_view, name="article")
]