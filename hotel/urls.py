from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView


from . import views
from django.urls import path, re_path

from .views import hotelSearch,GeneratePDF

app_name = 'hotel'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    # ex: /customer_list/
    path('about/', views.about, name='about'),
    path('hotels_list/', views.hotels_list, name='hotels_list'),
    path('<int:id>/<slug:slug>/', views.hotel_details, name='hotel_details'),
    path('<int:hotel_id>/<slug:hotel_slug>/<int:RoomNumber>/', views.room_details, name='room_details'),
    path('register/', views.register, name='register'),
    url(r'(?P<hotel_id>[0-9]+)/(?P<RoomNumber>[0-9]+)$/', views.bookroom, name='bookroom'),
    path('book/<int:hotel_id>/<int:RoomNumber>/', views.bookroom, name='bookroom'),
    url(r'^mybookings/$', views.mybookings, name='viewbookings'),
    url(r'^mybookings/cancel/(?P<id>[0-9]+)$', views.cancelbooking, name='cancelbooking'),
    url(r'^search$', hotelSearch.as_view(), name='hotelsearch'),
    url(r'^mybookings/(?P<id>[0-9]+)/pdf$', GeneratePDF.as_view(), name='gpdf'),

]