
from django.db import models
from django.utils import timezone


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    date = models.DateField(default=timezone.localdate)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title
