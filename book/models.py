from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images')

    def __str__(self):
        return self.name