from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=20, default='admin')
    tool_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
