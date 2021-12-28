from django.urls import path
from hotel import views

app_name = "Hotel"

urlpatterns = [
    path("search_room/", views.search_room, name="search-room"),
    path("search_room/<int:room_id>/", views.search_room, name="order-room"),
    path("my_account_hotel/", views.my_account_hotel, name="my-account-hotel"),
    # path("change_booking_date/", views.change_booking_date, name="change-booking-date"),
    path("change_booking_date/<int:room_id>/", views.change_booking_date, name="change-booking-date")

]