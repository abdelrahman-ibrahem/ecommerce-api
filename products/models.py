# products/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# add Category model 
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# create product model 
class Product(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    descrption = models.TextField()
    amount = models.PositiveIntegerField()
    isAvaliable = models.BooleanField(default=True)
    createdAt = models.DateField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    # Add slug field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.name # return value in admin page 


# create product images model 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.nama



class Review(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.CharField(max_length=255)

    def __str__(self):
        return self.owner.username


class Comment(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.owner.username



class Favorite(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.owner.username


# models for handle order operations

class Cart(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.owner.username

ORDER_STATUS = (
    ('pending', 'pending'),
    ('in the way', 'in the way'),
    ('deliverd', 'deliverd')
)

class Order(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, null=True, blank=True, choices=ORDER_STATUS, default="pending")
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    quantity = models.PositiveIntegerField()
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner.username