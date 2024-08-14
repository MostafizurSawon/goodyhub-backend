from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # router

router.register('products-list', views.ProductViewset) # router antena
router.register('category', views.CategoryViewset)
router.register('reviews', views.ReviewViewset) 

urlpatterns = [
    path('', include(router.urls)),
]