from django.urls import path
from . import views

urlpatterns = [
    path('', views.seat_list, name='seat_list'),
    path('book/<int:seat_id>/', views.book_seat, name='book_seat'),
]