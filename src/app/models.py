from django.db import models


class Route(models.Model):
    route_name = models.CharField(max_length=100, blank=False, null=False)
    route_number = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.route_name


class Bus(models.Model):
    bus_name = models.CharField(max_length=100,blank=False, null=False)
    bus_number = models.CharField(max_length=100, blank=False, null=False)
    routes = models.ManyToManyField(Route, through="Bus_Route",  related_name="buses")


    def __str__(self):
        return self.bus_name


class Bus_Route(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route.route_name}"



