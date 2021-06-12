from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('all_events/', views.all_events, name='all_events'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('list_venues/', views.list_venues, name='list_venues'),
    path('venue/<int:venue_id>', views.venue_details, name='venue_details'),
]
