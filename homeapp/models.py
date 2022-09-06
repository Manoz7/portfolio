from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', unique=True)
    category = models.CharField(max_length=50, default='Web Design')
    url = models.URLField()
    # desc = models.TextField(null=True)
    # desc2 = models.TextField(null=True)
    logo = models.ImageField(upload_to='logo')
    photo1 = models.ImageField(upload_to='portfolio')
    photo2 = models.ImageField(upload_to='portfolio')
    photo3 = models.ImageField(upload_to='portfolio', blank=True)
    con = HTMLField(default='', null=True)
    published_date = models.DateField(default='2022-02-02')
    
    def __str__(self) -> str:
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=50, default='')
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name