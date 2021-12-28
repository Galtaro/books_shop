from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("view_book", views.APIViewBook)

app_name: "Api"

urlpatterns = [
    path("add_like_to_comment_ajax/<int:comment_id>/", views.APIAddLike.as_view(), name ="add-like-to-comment"),
    path("books/", views.APIListBook.as_view(), name="list-book"),
    path("books/<int:pk>", views.APIBookDetail.as_view(), name="detail-book"),
    path("create_books/", views.APICreateBook.as_view(), name="create-book"),
] + router.urls
