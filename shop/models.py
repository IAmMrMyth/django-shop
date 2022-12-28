from django.db import models

# Create your models here.


class Color(models.Model):
    title = models.CharField(max_length=64)
    color_code = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to="images/categorty/")
    show_on_home_page = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=50)
    color = models.ManyToManyField(Color)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/%Y/%m/%d/")

    def __str__(self) -> str:
        return self.product.name


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}: {self.value} | {self.product.name}"
