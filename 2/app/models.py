from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    text = models.CharField(max_length=100, verbose_name="Title")
    kim = models.TextField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', verbose_name="Image", blank=True, null=True)

    def __str__(self):
        return self.name

    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class Proffesionalchef(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    maqom = models.CharField(max_length=50)
    description = models.TextField()
    fe = models.URLField()
    ins = models.URLField()
    x = models.URLField()
    inn = models.URLField()

    def __str__(self):
        return self.name
    
class Staywithus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    day = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Ourgallery(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image.url) 
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Xabar yuborilgan vaqt

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_hours = models.CharField(max_length=255, default="Mon-Sat: 11AM - 23PM; Sunday: Closed")

    def __str__(self):
        return self.address