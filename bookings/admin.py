from django.contrib import admin
from .models import Seat

# Register your models here.
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_booked', 'booked_by')
    list_filter = ('is_booked',)
    fields = ('number', 'is_booked', 'booked_by')
    readonly_fields = ()