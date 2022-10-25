from django.urls import path

from .views import create, retrieve, update, delete

app_name = "accounts"

urlpatterns = [
    path('create/', create, name="create"),
    path('retrieve/', retrieve, name="retrieve"),
    path('update/', update, name="update"),
    path('delete/', delete, name="delete"),
]