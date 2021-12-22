from django.urls import path
from hotel import views

app_name = "Hotel"

urlpatterns = [
    path("search_room/", views.search_room, name="search-room"),
    path("search_room/<int:room_id>/", views.search_room, name="order-room"),
    path("my_account/", views.my_account, name="my-account")
]