from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events_list/', views.events_list, name='events_list'),
    path('event_add/', views.event_add, name='event_add'),
    path('event_upd/<int:event_id>', views.event_upd, name='event_upd'),
    path('event_del/<int:event_id>', views.event_del, name='event_del'),
    path('venues_list/', views.venues_list, name='venues_list'),
    path('venue/<int:venue_id>', views.venue_details, name='venue_details'),
    path('venue_add/', views.venue_add, name='venue_add'),
    path('venue_upd/<int:venue_id>', views.venue_upd, name='venue_upd'),
    path('venue_del/<int:venue_id>', views.venue_del, name='venue_del'),
    path('events_save_txt', views.events_save_txt, name='events_save_txt'),
    path('events_save_csv', views.events_save_csv, name='events_save_csv'),
    path('events_save_pdf', views.events_save_pdf, name='events_save_pdf'),
]


