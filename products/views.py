# products/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import generics
from products.models import Cart, Category, Favorite, Order, Product, Review, Comment
from .serializers import (
    CartSerializer, CategorySerializer, FavoriteSerializer, ProductSerializer,
    ReviewSerializer, CommentSerializer, OrderSerializer
)
from rest_framework import permissions
from permissions.userPermissions import IsOwner
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination

# add pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination



class ProductView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(slug=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except:
            return Response({
                "message": "Page not found"    
            })



class ListOrCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
            permissions.IsAuthenticated
        ]



class ViewReviewOrUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ] 


class ListCommentsReview(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
            permissions.IsAuthenticated
        ]


class ViewOrUpdateOrDeleteComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ]



class ListFavoriteProduct(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ]



class RemoveProductFromFavorite(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ]

# Handle cart
class ListMyCart(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ]

class AddToCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateOrRemoveProductFromCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            IsOwner
        ]


# for admin role
class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            permissions.IsAdminUser
        ]

class RetreveOrUpdateOrDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
            permissions.IsAuthenticated,
            permissions.IsAdminUser
        ]


class ListOrCreateCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
            permissions.IsAdminUser
        ]

class RetreveOrUpdateOrRemoveCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
            permissions.IsAdminUser
        ]

# create function for sending message after create order 
def send_message(product, quantity, email):
    pass


# TODO Handle order operations
class CreateOrder(APIView):
    def post(self, request):
        data = request.data
        cartItem = Cart.objects.filter(
                owner = request.user,
                ordered=False
            )
        # print(products)
        # print(request.data)
        for product in cartItem:
            order = Order.objects.create(
                    owner=request.user,
                    product=product.product,
                    phone=data['phone'],
                    email=data['email'],
                    address=data['address'],
                    quantity= product.quantity
                )
            order.save()
            product.ordered = True
            product.save()
            product.product.amount = product.product.amount - product.quantity
            product.product.save()
            # TODO solve sending message problem and add to the CreateOrder class 
            # send_message(product.product, product.quantity, data['email'])
            
        
        return Response({
                "message": "created"
            }, status=status.HTTP_201_CREATED)

class ListOrders(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
            permissions.IsAdminUser
        ]

class RetreveOrUpdateOrDeleteOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
            permissions.IsAdminUser
        ]


'''
test create order 
{
    "phone":"01002761582",
    "email":"abdo.ibrahem1122@gmail.com",
    "address":"portsaid"
}
'''