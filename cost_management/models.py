from django.db import models

# Create your models here.
class Expense(models.Model):
    total_amount=models.IntegerField()
    amount = models.IntegerField()
    purpose = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose
