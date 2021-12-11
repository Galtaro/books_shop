from django.shortcuts import render, redirect
from myapp.models import Book, RateBookUser, OrderBookUser, Comment
from django.db.models import Avg, Sum, Prefetch, Count


def hello(request):
    query_1 = Comment.objects.annotate(likes=Count("like"))
    query_2 = Book.objects.annotate(
        avg_rate=Avg("rate_book_user_book__rate"),
        total_order=Sum("order_book_user_book__count")
        ).prefetch_related("authors", Prefetch("comments", query_1), "comments__user").select_related("country")
    return render(request, "index.html", {"books": query_2})


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


def add_comment(request, book_id):
    if request.user.is_authenticated:
        Comment.objects.create(
            user_id=request.user.id,
            text=request.POST.get("comment"),
            book_id=book_id
        )
    return redirect("main-page")


def delete_comment(request, comment_id):
    if request.user.is_authenticated:
        query_set = Comment.objects.filter(id=comment_id)
        if query_set.exists():
            if query_set.first().user.id == request.user.id:
                query_set.delete()
    return redirect("main-page")


def update_comment(request, comment_id):
    if request.user.is_authenticated:
        comment_query = Comment.objects.filter(id=comment_id)
        if comment_query.exists():
            if request.method == "GET":
                return render(request, "comment_form.html", {"comment": comment_query.first()})
            if request.method == "POST":
                comment_query.update(text=request.POST.get("comment"))
    return redirect("main-page")
