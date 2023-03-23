from django.urls import path
from .views import index, favorites, add_favorite, get_favorite

urlpatterns = [
    path('', index, name = 'home'),
    path('favorites/', favorites, name='favorites'),   
    path('favourite/<str:location_name>/', get_favorite, name = 'get_favorite'),
    path('add_favorite/<str:location_name>/', add_favorite, name='add_favorite'),
]
