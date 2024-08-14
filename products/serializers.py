from rest_framework import serializers
from . import models
# from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Product
        fields = '__all__'












# class PlantSerializer(serializers.ModelSerializer):
#     # user field for read operations
#     user = serializers.StringRelatedField(read_only=True)
#     # user field for write operations
#     user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

#     class Meta:
#         model = models.Plant
#         fields = ['title', 'price', 'category', 'user', 'user_id', 'image', 'description', 'quantity', 'created']  # Exclude 'sold'

#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
