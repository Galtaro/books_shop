from django.core import validators
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    class Meta:
        db_table = "book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(max_length=100, db_index=True)
    authors = models.ManyToManyField(User, related_name="books")
    publish_date = models.DateField(auto_now=True)
    text = models.TextField()
    rate = models.ManyToManyField(User, related_name="rated_books", through="myapp.RateBookUser")
    order = models.ManyToManyField(User, related_name="ordered_books", through="myapp.OrderBookUser")
    price = models.DecimalField(max_digits=4, decimal_places=2)

class RateBookUser(models.Model):
    class Meta:
        unique_together = ("user", "book")
    rate = models.PositiveIntegerField(
        default=1,
        validators=[validators.MaxValueValidator(5), validators.MinValueValidator(1)]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class OrderBookUser(models.Model):
    count = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)