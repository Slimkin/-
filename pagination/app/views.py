from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, mode='r', encoding='cp1251') as f:
        stations_list = list(csv.DictReader(f))

    current_page = int(request.GET.get('page', 1))
    pagi = Paginator(stations_list, 10)
    stations = pagi.get_page(current_page)

    next_page_url, prev_page_url = None, None
    if stations.has_next():
        next_page_url = f'?page={stations.next_page_number()}'
    if stations.has_previous():
        prev_page_url = f'?page={stations.previous_page_number()}'


    return render_to_response('index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

