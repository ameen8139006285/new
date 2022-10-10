from django.db import models


# Create your models here.
class about(models.Model):
    head_title = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic = models.ImageField()
    age = models.IntegerField()
    website = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    phone = models.IntegerField()
    myemail = models.EmailField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class services(models.Model):
    title_service_desc = models.TextField()
    subtitle= models.CharField(max_length=100)
    subtitle_desc = models.TextField()
    photo_category = models.CharField(max_length=100)
    photo_category_price = models.IntegerField()
    reviews_desc = models.TextField()
    reviewer_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.reviewer_name
class contact(models.Model):
    clientname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.clientname
    