from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .forms import *
from .models import Hotels,Rooms,Images,Reservation
from django.utils import timezone
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from .utils import render_to_pdf

# Create your views here.
now = timezone.now()


def home(request):
    return render(request, 'hotel/home.html', {'hotel': home})


def about(request):
    return render(request, 'hotel/about.html', {'hotel': home})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'registration/registerdone.html',
                          {'form': form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required()
def hotels_list(request):
    hotels = Hotels.objects.all()
    images = Images.objects.all()
    return render(request,'hotel/hotels_list.html',{'hotels':hotels,'images': images})

@login_required()
def hotel_details(request, id, slug):
    hotel = get_object_or_404(Hotels,id=id, slug=slug,)
    images = Images.objects.filter(hotel=hotel)
    rooms = Rooms.objects.filter(hotel=hotel)
    return render(request, 'hotel/hotel_details.html',
                  {'hotel': hotel,'images':images,'rooms':rooms})

@login_required()
def room_details(request, hotel_id, hotel_slug,RoomNumber,):
    hotel = get_object_or_404(Hotels,id=hotel_id, slug=hotel_slug)
    room = Rooms.objects.get(hotel=hotel,RoomNumber=RoomNumber)
    return render(request, 'hotel/room_details.html',
                  {'hotel': hotel,'room':room })

@login_required()
#Shows the user thier previous bookings.
def mybookings(request):
    bookings = Reservation.objects.filter(user = request.user)
    return render(request, 'hotel/mybookings.html', {'bookings':bookings,'now': datetime.datetime.now()})


# Allows a user to cancel their previous bookings , deleting a booking onclick.
@login_required()
def cancelbooking(request,id):
    booking = get_object_or_404(Reservation,id = id)
    booking.delete()
    return redirect('hotel:viewbookings')

@login_required()
def bookroom(request,hotel_id,RoomNumber):
    if request.method == 'POST':
        form = Booking(request.POST)
        CheckinDate = request.POST['CheckIn']
        print("check in", CheckinDate)
        CheckoutDate = request.POST['CheckOut']
        print("check out", CheckoutDate)
        Checkin = datetime.datetime.strptime(CheckinDate, "%m/%d/%Y").date()
        Checkout = datetime.datetime.strptime(CheckoutDate, "%m/%d/%Y").date()
        if form.is_valid():
            currentuser = request.user
            hotel = Hotels.objects.get(id=hotel_id)
            room = Rooms.objects.get(RoomNumber=RoomNumber)
            # check wether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(room=room, CheckIn__lte=Checkin, CheckOut__gte=Checkin).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(room=room, CheckIn__lte=Checkout, CheckOut__gte=Checkout).exists()

            case_3 = Reservation.objects.filter(room=room, CheckIn__gte=Checkin, CheckOut__lte=Checkout).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                messages.error(request, 'Room is not available on that dates')
                return render(request, "hotel/booking.html",
                              {'form': form})

            reservation = form.save(commit=False)
            reservation.user=currentuser
            reservation.hotel=hotel
            reserved = False
            timedeltaSum = Checkout - Checkin
            print("timedeltaSum", timedeltaSum)
            StayDuration = timedeltaSum.days
            print("StayDuration", StayDuration)
            price = room.Price
            TotalCost = StayDuration * price
            print("TotalCost", TotalCost)
            reservation.totalPrice=TotalCost
            reservation.created_date = timezone.now()
            reservation.room = room
            reservation.save()
            return render(request, 'hotel/bookingsuccess.html',
                              {'reservation': reservation})
    else:
        form = Booking()
    return render(request, 'hotel/booking.html', {'form': form})




## Generates a PDF using the render help function and outputs it as invoice.html
class GeneratePDF(View):
    def get(self,request, *args, **kwargs):
        reservation = Reservation.objects.get(id= self.kwargs['id'])
        template = get_template('hotel/invoice.html')
        context = {"reservation":reservation}
        html = template.render(context)
        pdf = render_to_pdf('hotel/invoice.html', context)
        return HttpResponse(pdf,content_type='application/pdf')

class hotelSearch(View):
    def get(self,request):
        return render(request, 'hotel/search.html')
    def post(self,request):
        print("Searchterm entered post ")
        #Searchterm = request.POST.get("searchitem")
        Searchterm=request.POST['searchitem']
        print("Searchterm",Searchterm)
        if Searchterm:
            hotels_list = Hotels.objects.filter(Q(City__icontains=Searchterm) | Q(Country__icontains=Searchterm)
            | Q(state__contains=Searchterm)| Q(Name__icontains=Searchterm))
            print("hotels_list",hotels_list)
            if hotels_list:
                context = {'hotels': hotels_list}
                return render(request, 'hotel/hotels_list.html', context)
            else:
                messages.error(request,'No results found')
        return render(request, 'hotel/search.html')
