from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Stores all the hotel details and is used to query hotels.
class Hotels(models.Model):
    Name = models.CharField(max_length  = 255)
    Description = models.TextField(max_length=700)
    Amenities = models.TextField(max_length=150)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    TelephoneNumber = models.CharField(max_length=12)
    slug = models.SlugField(max_length=100, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
         return self.Name

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('hotel:hotel_details', args=[self.id, self.slug])


class Images(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='imagesofhotel')
    image = models.ImageField(upload_to='hotelimages/%Y/%m/%d', blank=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


# Stores the Hotels rooms
class Rooms(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    RoomNumber=models.IntegerField(max_length=10,primary_key=True)
    RoomType = models.CharField(max_length = 255)
    Capacity = models.IntegerField(default = 0)
    BedOption = models.CharField(max_length = 255)
    RoomSize=models.CharField(max_length=10)
    Amenities = models.TextField(max_length=150)
    Price= models.IntegerField(default = 0)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='hotelroomimages/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.RoomType

    def get_absolute_url(self):
        return reverse('hotel:room_details', args=[self.hotel.id,self.hotel.slug,self.RoomNumber])


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    comment = models.CharField(max_length  = 255)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
         return self.comment

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

#Create a Reservation Model which stores booking details


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    guestFirstName = models.CharField(max_length  = 255)
    guestLastName = models.CharField(max_length  = 255)
    email = models.EmailField(max_length=70)
    phonenumber=models.IntegerField(max_length=10)
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    totalPrice = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Reservation'

    def __str__(self):
         return self.user.username


