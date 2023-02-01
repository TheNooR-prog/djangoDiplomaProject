from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish
from .forms import UserReservationForm


def main_page(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    reservation = UserReservationForm()

    data = {'categories': categories,
            'dishes': dishes,
            'reservation_form': reservation,
            }

    return render(request, 'main_page.html', context=data)


