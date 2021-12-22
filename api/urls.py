from django.urls import path
from api import views

app_name: "Api"
urlpatterns = [
    path("add_like_to_comment_ajax/<int:comment_id>/", views.APIAddLike.as_view, name ="add-like-to-comment")

]