from django.contrib import admin
from .models import (
    BusStructure,
    Bus,
    Schedule,
    BusSchedule
)

# Register your models here.
admin.site.register(BusStructure)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(BusSchedule)
