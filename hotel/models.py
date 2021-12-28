from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

    choices_room = [
        (1, "однокомнатная" ),
        (2, "двухкомнатная"),
        (3, "трехкомнатная")
    ]
    capacity = models.PositiveSmallIntegerField(verbose_name="колличество комнат", db_index=True, choices=choices_room)
    price_for_day = models.DecimalField(verbose_name="цена за день", max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    number = models.PositiveSmallIntegerField(verbose_name="номер", db_index=True)
    condition = models.BooleanField(verbose_name="кондиционер", default=False)
    image = models.ImageField(verbose_name="картинка", upload_to="room/%Y")

    def __str__(self):
        return str(self.number)


class OrderRoom(models.Model):
    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
    room = models.ForeignKey(Room, verbose_name="комнаты", on_delete=models.CASCADE, related_name="ordered_room")
    user = models.ForeignKey(User, verbose_name="клиент", on_delete=models.CASCADE, related_name="ordered_user")
    price = models.DecimalField(verbose_name="цена", max_digits=5, decimal_places=2, blank=True)
    start_date = models.DateTimeField(verbose_name="дата заселения")
    end_date = models.DateTimeField(verbose_name="дата выселения")
    date = models.DateField(verbose_name="дата заказа", auto_now_add=True)

    def save(self, **kwargs):
        self.price = (self.end_date - self.start_date).days * self.room.price_for_day
        super().save(**kwargs)

    def __str__(self):
        return f"{self.room.number} {self.start_date} - {self.end_date}"





