from django.db import models

# Create your models here.


class Logo(models.Model):
    name = models.CharField(max_length=20, default="hello")
    logo_image = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.name



class Slider(models.Model):
    name = models.CharField(max_length=20, default='hello')
    slider_image = models.ImageField(
        upload_to='slider/', blank=True, null=True)
    title = models.CharField(max_length=150, default=" ")
    sub_title = models.TextField()

    def __str__(self):
        return self.name


class Propuler_categories(models.Model):
    name = models.CharField(max_length=20, default='hello')
    title = models.CharField(max_length=40, default='hello')
    sub_title = models.CharField(max_length=80, default='hello')
    categories_background_image = models.ImageField(
        upload_to='slider/', blank=True, null=True)
    categories_image = models.ImageField(
        upload_to='slider/', blank=True, null=True)

    def __str__(self):
        return self.name


class Producat(models.Model):
    name = models.CharField(max_length=20, default='hello')
    title = models.CharField(max_length=40, default='hello')
    
    status_categories = models.CharField(max_length=40, default='hello')
    
    availability = models.BooleanField(blank=False,default=True)
    producat_tags = models.CharField(max_length=30,null=True,default="hello")
    
    producat_image_1 = models.ImageField(upload_to='producats/', blank=True, null=True)
    producat_image_2 = models.ImageField(upload_to='producats/', blank=True, null=True)
    producat_image_3 = models.ImageField(upload_to='producats/', blank=True, null=True)
    producat_image_4 = models.ImageField(upload_to='producats/', blank=True, null=True)
    
    producat_description = models.TextField(null = True, blank = True, default="helloooooo")
    
    discount_percent =  models.CharField(max_length=4, default='30%',null=True)
    prices =  models.CharField(max_length=10, default='0000')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=20, default="hello")
    ss_coustomer_review = models.ImageField(upload_to='coustomer_review/', blank=True, null=True)

    def __str__(self):
        return self.name
