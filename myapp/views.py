from django.shortcuts import render, redirect
from myapp.models import Book, RateBookUser, OrderBookUser
from django.db.models import Avg, Sum


def hello(request):
    query = Book.objects.annotate(
        avg_rate=Avg("rate_book_user_book__rate"),
        total_order=Sum("order_book_user_book__count")
        ).prefetch_related("authors")
    return render(request, "index.html", {"books": query})


def add_rate(request, rate, book_id):
    if request.user.is_authenticated:
        RateBookUser.objects.update_or_create(user_id=request.user.id, book_id=book_id, defaults={"rate":rate})
    return redirect("main-page")


def order_book(request, book_id):
    if request.user.is_authenticated:
        OrderBookUser.objects.create(
            count=request.POST.get("count"),
            user_id=request.user.id,
            book_id=book_id
        )
    return redirect("main-page")