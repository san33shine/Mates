from django.urls import path
from .views.indexes.index import Index

app_name = 'wandermates'
urlpatterns = [
    path("", Index.as_view(), name = 'wandermates_index'),
]