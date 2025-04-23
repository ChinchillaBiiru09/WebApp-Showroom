from django.db import models

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    car_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.description