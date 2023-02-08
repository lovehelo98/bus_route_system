from django.shortcuts import render
from .models import Bus, Route, Bus_Route
from .tables import BusTable, BusRouteTable, RouteTable, RouteBusTable
from django.db.models import Count, QuerySet


# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_buses(request):
    table = BusTable(Bus.objects.annotate(number_of_routes=Count('routes')))
    context = {
        'table': table
    }
    return render(request, 'table.html', context)



def get_bus_routes(request, id):
    bus = Bus.objects.get(pk=id)
    bus_routes = Bus_Route.objects.filter(bus=bus)
    table = BusRouteTable(bus_routes)
    context = {
        'table' : table
    }
    return render(request, 'table.html', context)


def get_routes(request):
    routes = Route.objects.annotate(numbers_of_buses=Count('buses'))
    table = RouteTable(routes)
    context = {
        'table' : table
    }
    return render(request, 'table.html', context)

def get_route_buses(request, id):
    route = Route.objects.get(pk=id)
    bus_routes = Bus_Route.objects.filter(route=route)
    table = RouteBusTable(bus_routes)
    context = {
        'table' : table
    }
    return render(request, 'table.html', context)
