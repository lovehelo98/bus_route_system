import django_tables2 as tables
from .models import Bus, Route, Bus_Route

class BusTable(tables.Table):
    number_of_routes= tables.TemplateColumn('<a href="{% url "get_bus_routes" record.pk %}">{{ record.number_of_routes }}</a>', verbose_name="Number of routes this bus runs on" )

    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus_name","bus_number", "number_of_routes" )


class BusRouteTable(tables.Table):
    route_name = tables.TemplateColumn('{{record.route.route_name}}', verbose_name="Route name")
    route_number = tables.TemplateColumn('{{record.route.route_number}}', verbose_name="Route number")

    class Meta:
        model = Bus_Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("route_name","route_number", "from_time", "to_time")

class RouteTable(tables.Table):
    numbers_of_buses= tables.TemplateColumn('<a href="{% url "get_route_buses" record.pk %}">{{ record.numbers_of_buses}}</a>', verbose_name='Number of buses runing on this route' )

    

    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("route_name","route_number", "numbers_of_buses")

class RouteBusTable(tables.Table):
    bus_name = tables.TemplateColumn('{{record.bus.bus_name}}', verbose_name="Bus name")
    bus_number = tables.TemplateColumn('{{record.bus.bus_number}}', verbose_name="Bus number")

    class Meta:
        model = Bus_Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus_name","bus_number", "from_time", "to_time")