from django.db import models

# Create your models here.
class Expense(models.Model):
    id=models.IntegerField(primary_key=True)
    total_amount=models.IntegerField(blank=True,null=True)
    amount = models.IntegerField()
    purpose = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose
