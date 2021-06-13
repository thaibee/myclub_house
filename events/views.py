import calendar
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from .models import Event, Venue
from .forms import VenueForm, EventForm
import csv


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Andrey'
    month = month.title()
    month_n = list(calendar.month_name).index(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month_n)
    current_time = datetime.now().strftime('%I:%M:%p')
    current_year = datetime.now().year
    next_month = list(calendar.month_name)[datetime.now().month + 1]

    return render(request, 'events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'current_time': current_time,
        'current_year': current_year,
        'next_month': next_month,
    })


def venues_list(request):
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    list_venues = Venue.objects.all
    return render(request, 'events/venues_list.html', {
        'next_month': next_month,
        'list_venues': list_venues,
    })


def venue_details(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/venue_details.html', {
        'venue': venue,
        'next_month': next_month,
    })


def venue_add(request):
    submitted = False
    if request.POST:
        form = VenueForm(request.POST)
        if form.is_valid:
            submitted = True
            form.save()
    else:
        form = VenueForm()
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/venue_add.html', {
        'next_month': next_month,
        'form': form,
        'submitted': submitted
    })


def venue_upd(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venues')
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/venue_upd.html', {
        'form': form,
        'next_month': next_month,
    })


def venue_del(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venues_list')


def events_list(request):
    event_list = Event.objects.all().order_by('name')
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/events_list.html', {
        'event_list': event_list,
        'next_month': next_month,
    })


def event_add(request):
    submitted = False
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid:
            submitted = True
            form.save()
    else:
        form = EventForm()
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/event_add.html', {
        'next_month': next_month,
        'form': form,
        'submitted': submitted
    })


def event_upd(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events_list')
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/event_upd.html', {
        'form': form,
        'next_month': next_month,
    })


def event_del(request, venue_id):
    event = Event.objects.get(pk=venue_id)
    event.delete()
    return redirect('events_list')


def events_save_txt(request):
    events = Event.objects.all()
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="events.txt"'
    for i in events:
        response.writelines(f'{i.name}\n{i.venue}\n{i.event_date}\n{i.event_time}\n\n\n')
    return response


def events_save_csv(request):
    events = Event.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="events.csv"'
    writer = csv.writer(response, delimiter='\t')
    writer.writerow(['Name', 'Venue', 'Date', 'Time'])
    for i in events:
        writer.writerow([i.name, i.venue, i.event_date, i.event_time])
    return response
