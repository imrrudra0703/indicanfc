from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="Details")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Exhibition(models.Model):
    name = models.CharField(max_length=100, blank=False)
    logo1 = models.ImageField(upload_to="", blank=False)
    logo2 = models.ImageField(upload_to="Exhibition", blank=False)
    image1 = models.ImageField(upload_to="Exhibition", blank=False)
    image2 = models.ImageField(upload_to="Exhibition", blank=False)
    image3 = models.ImageField(upload_to="Exhibition", blank=False)
    image4 = models.ImageField(upload_to="Exhibition", blank=False)
    image5 = models.ImageField(upload_to="Exhibition", blank=False)
    video = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Open_Mic(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=12, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    
    types = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=1000, blank=False)
    link = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return self.fullname

class Newsletter(models.Model):
    email = models.EmailField(max_length=100, blank=False)

    def __str__(self):
        return self.email

class Comment(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    comment = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.comment
