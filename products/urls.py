from django.urls import path 
from . import views


urlpatterns = [
    path('', views.ListProducts.as_view()),
    path('product-details/<slug:pk>/', views.ProductView.as_view()),
    path('reviews/', views.ListOrCreateReview.as_view()),
    path('reviews/<int:pk>', views.ViewReviewOrUpdateOrDelete.as_view()),
    path('comments/', views.ListCommentsReview.as_view()),
    path('comments/<int:pk>/', views.ViewOrUpdateOrDeleteComment.as_view()),
    path('favorites/', views.ListFavoriteProduct.as_view()),
    path('favorites/remove/<int:pk>', views.RemoveProductFromFavorite.as_view()),
    path('my-cart/', views.ListMyCart.as_view()),
    path('add-to-cart/', views.AddToCart.as_view()),
    path('update-cart/<int:pk>', views.UpdateOrRemoveProductFromCart.as_view()),
    path('admin/create-product/', views.CreateProduct.as_view()),
    path('admin/delete-product/<int:pk>', views.RetreveOrUpdateOrDeleteProduct.as_view()),
    path('admin/create-category/', views.ListOrCreateCategories.as_view()),
    path('admin/create-category/<int:pk>', views.RetreveOrUpdateOrRemoveCategory.as_view()),
    path('create-order/', views.CreateOrder.as_view()),
    path('orders/', views.ListOrders.as_view()),
    path('orders/<int:pk>/', views.RetreveOrUpdateOrDeleteOrder.as_view())
]