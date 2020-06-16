from django.db import models
from signup.models import Customer

# Create your models here.
class Comments(models.Model):
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table="Comments"

    def __str__(self):
        return self.comment