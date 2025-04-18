from django.urls import path
from .views import quote_gallery, like_quote

urlpatterns = [
    path('', quote_gallery, name='quote_gallery'),
    path('like/<int:quote_id>/', like_quote, name='like_quote'),
]
