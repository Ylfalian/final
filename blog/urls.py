from django.urls import path
from .views import render_posts, post_detalle



urlpatterns = [
    path("",render_posts,name="posts"),
    path("<int:post_id>", post_detalle, name="post_detalle"),
]

