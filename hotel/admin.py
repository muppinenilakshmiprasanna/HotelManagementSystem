from django.contrib import admin

# Register your models here.
from django.db import models

from .models import Hotels,Rooms,Reservation,Images


class ImageInline(admin.TabularInline):
    model = Images


class HotelsList(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Address','City','Country','TelephoneNumber')
    list_filter = ('Name', 'state', 'Country')
    search_fields = ('Name','City','Country','state')
    ordering = ['Name']
    prepopulated_fields = {'slug': ('Name',)}
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'image',]


class RoomsList(admin.ModelAdmin):
    list_display = ['RoomNumber','RoomType', 'hotel', 'Capacity','BedOption','RoomSize','Amenities', 'Price']
    list_filter = ['RoomType', 'hotel','Price',]
    list_editable = ['Price','Capacity',]
    prepopulated_fields = {'slug': ('RoomNumber',)}


admin.site.register(Hotels,HotelsList)
admin.site.register(Rooms,RoomsList)
admin.site.register(Reservation)
admin.site.register(Images,ImageAdmin)

