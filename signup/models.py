from django.db import models

# Create your models here.
class Customer(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other')
    )

    id =  models.CharField(max_length = 200, primary_key=True)
    email = models.CharField(max_length = 200, null = True)
    password = models.CharField(max_length = 200, null = False)
    gender =  models.CharField(max_length = 200, null = True, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.id

    class Meta:
        db_table="Customers"

# class Comments(models.Model):
#     customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
#     comment = models.CharField(max_length = 200, null = True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     class Meta:
#         db_table="Comments"

#     def __str__(self):
#         return self.comment

# class Comment_list(models.model):
#     customer = models.ForeignKey(Customer, null = False, on_delete=models.SET_NULL)
#     comment = models.ForeignKey(Comments, null = False, on_delete=models.SET_NULL)