from django.urls import path
from myapp import views


urlpatterns = [
    path("hello/", views.hello, name="main-page"),
    path("add_rate/<int:rate>/<int:book_id>/", views.add_rate, name="add-rate"),
    path("order_book/<int:book_id>/", views.order_book, name="order-book"),
]