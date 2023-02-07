from django.urls import path
from . import views
from .views import index, get_buses, get_bus_routes, get_routes, get_route_buses

urlpatterns = [
    path('', index, name='index'),
    path("buses/", get_buses, name="buses"),
    path("bus/<int:id>/routes/", get_bus_routes, name="get_bus_routes"),
    path("routes/", get_routes, name="routes"),
    path("route/<int:id>/buses/", get_route_buses, name="get_route_buses"),
]