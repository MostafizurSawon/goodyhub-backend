from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ProductPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = ProductPagination
    search_fields = [
        'name',                  
        'description',            
        'category__name',         
        'user__first_name',       
        'user__last_name',        
        'user__username',         
        'user__email',            
        'comments__user__username',  
    ]
    # permission_classes = [IsAuthenticated]  # Enforce authentication

    def perform_create(self, serializer):
        # Assign the current user as the owner of the Product
        serializer.save(user=self.request.user)
        # serializer.save()
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer



