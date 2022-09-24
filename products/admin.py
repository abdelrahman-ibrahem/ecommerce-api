# products/admin.py
from django.contrib import admin
from .models import Product, ProductImage, Review, Comment, Favorite, Cart, Order, Category

class ProducctImageCustom(admin.TabularInline):
    model = ProductImage

class CommentInline(admin.TabularInline):
    model = Comment

class CustomReview(admin.ModelAdmin):
    inlines = [
            CommentInline
        ]
    list_display = ['owner', 'review', 'product']


class ReviewInline(admin.TabularInline):
    model = Review


class CustomProduct(admin.ModelAdmin):
    inlines = [
            ProducctImageCustom,
            ReviewInline
        ]
    list_display = [
            'name', 'isAvaliable','createdAt', 'updatedAt', 'amount'
        ]

class CustomFavorite(admin.ModelAdmin):
    list_display = ['owner', 'product']

class CustomCommnet(admin.ModelAdmin):
    list_display = ['owner', 'content', 'review']



class CustomCart(admin.ModelAdmin):
    list_display = ['owner', 'product', 'quantity', 'ordered']


class CustomOrder(admin.ModelAdmin):
    list_display = ['owner', 'product', 'quantity', 'email', 'phone', 'address', 'status']

admin.site.register(Product, CustomProduct)
admin.site.register(Review, CustomReview)
admin.site.register(Comment, CustomCommnet)
admin.site.register(Favorite, CustomFavorite)
admin.site.register(Cart, CustomCart)
admin.site.register(Order, CustomOrder)
admin.site.register(Category)