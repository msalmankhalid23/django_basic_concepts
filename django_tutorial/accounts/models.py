from django.db import models

# Create Custmer class with field name, phone, email, date_created

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Features(models.Model):
   
    CATEGORIES = (('cat1', 'category 1'), ('cat2', 'category 2'), ('cat3', 'category 3'))

    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    url = models.CharField(max_length=200, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name