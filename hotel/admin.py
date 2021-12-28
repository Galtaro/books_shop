from django.contrib import admin
from hotel.models import Room, OrderRoom


class OrderRoomInLine(admin.StackedInline):
    model = OrderRoom
    readonly_fields = ["price"]


class RoomAdmin(admin.ModelAdmin):
    inlines = [OrderRoomInLine]


admin.site.register(Room, RoomAdmin)

