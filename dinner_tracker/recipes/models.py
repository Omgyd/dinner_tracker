from django.db import models
from django.shortcuts import render, redirect, reverse

# Create your models here.


class Recipe(models.Model):
    ONESTAR = "1."
    TWOSTAR = "2."
    THREESTAR = "3."
    FOURSTAR = "4"
    FIVESTAR = "5"
    MY_CHOICES = [
        (ONESTAR, "One Star"),
        (TWOSTAR, "Two Star"),
        (THREESTAR, "Three Star"),
        (FOURSTAR, "Four Star"),
        (FIVESTAR, "Five Star"),
        ]
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=1000)
    instructions = models.TextField(blank=True)
    rating = models.CharField(max_length=10, choices=MY_CHOICES)

    def get_absolute_url(self):
        return reverse("create_recipe")



