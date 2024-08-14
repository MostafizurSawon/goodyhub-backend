from django.db import models
from django.contrib.auth.models import User
# from user_profile.models import UserProfile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(null=True, blank=True,default=4.99,max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.title} of Mr. {self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"User : {self.reviewer.user.first_name} ; Plant: {self.Plant.user.first_name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.Plant.title}"