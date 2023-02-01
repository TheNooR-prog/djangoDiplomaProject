from django.core.validators import RegexValidator
from django.db import models
import uuid
import os

import djangoDiplomaProject.settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class UserReservation(models.Model):
    email_re = RegexValidator(regex=r'^[0-9a-zA-z]+([-\.]?[0-9a-zA-z_])*@[0-9a-zA-z]+(\.?[0-9a-zA-z])*$',
                              message='Email could include "0-9,a-z,A-Z,_,-,." only')
    mobile_re = RegexValidator(regex=r'^(\d{3}[- ]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, validators=[email_re])
    phone = models.CharField(max_length=15, validators=[mobile_re])
    date = models.DateField()
    time = models.TimeField()
    number_people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time', '-is_processed', )

    def __str__(self):
        return f'{self.date} {self.time} | {self.name} {self.phone}: {self.message[:50]}'
