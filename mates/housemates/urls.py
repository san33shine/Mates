from django.urls import path
from .views.indexes.index import Index

app_name = 'housemates'
urlpatterns = [
    path("", Index.as_view(), name = 'housemates_index'),
]