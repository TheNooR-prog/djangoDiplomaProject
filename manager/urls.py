from django.urls import path
from .views import reservations_list, update_reservation

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve')
]

