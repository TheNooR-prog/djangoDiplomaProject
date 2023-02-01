from django.contrib import admin
from .models import Category, Dish, UserReservation

# Register your models here.
admin.site.register(Category)
admin.site.register(UserReservation)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name', ), }


