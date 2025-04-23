from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    # color = models.CharField(max_length=25)
    description = models.TextField()
    # image = models.ImageField(upload_to='car_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.brand
