from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    def save(self, *args, **kwargs):
        if self.role == self.ADMIN and not AuthUser.objects.filter(username=self.username).exists():
                AuthUser.objects.create_superuser(username=self.username, password=self.password)
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
        
    
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    summary = models.TextField(blank=True)  
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.book.title}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.last_updated = timezone.now()
        self.book.save()   