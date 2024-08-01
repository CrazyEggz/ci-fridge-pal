from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    best_before = models.DateTimeField(null=True, blank=True)
    use_by = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey('Location')
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name