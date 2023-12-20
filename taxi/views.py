from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListCreateAPIView, ListAPIView, CreateAPIView

from .filters import DriverFilter
from .models import Driver, Seat, Booking
from .pagination import CustomPagination
from .serializers import SeatModelSerializer, DriverModelSerializer, BookingSerializer


# Search

class CarSearchAPIView(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DriverFilter
    pagination_class = CustomPagination



class SeatCreateAPIView(ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DriverCreateAPIView(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverModelSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


#  Driver Update and Delete
class DriverDetailAPIView(UpdateAPIView, DestroyAPIView):
    """
    {
      "first_name": "Ali",
      "last_name": "Aliyev",
      "phone": "123456789",
      "account_tg": "aliyevvvv03",
      "model": "Malibu",
      "from_place": "Tashkent",
      "to_place": "Bukhara",
      "date": "2023-12-31",
      "price": "1000",
      "seat": [
        {
          "seat": 1,
          "is_booked": true
        },
        {
          "seat": 2,
          "is_booked": false
        }
      ]
    }
    """
    queryset = Driver.objects.all()
    serializer_class = DriverModelSerializer
    permission_classes = [permissions.IsAuthenticated]



# Booking Post

class BookingCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    """
           {
      "first_name": "Ali",
      "last_name": "Aliyev",
      "seat": [
        {"id": 1, "is_booked": true, "seat": 2},
        {"id": 3, "is_booked": true, "seat": 4}
      ]
    }
    """
    serializer_class = BookingSerializer


class MyBookingsAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDetailAPIView(UpdateAPIView, DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    """
           {
      "first_name": "Ali",
      "last_name": "Aliyev",
      "phone": "123456789",
      "seat": [
        {"id": 1, "is_booked": true, "seat": 2},
        {"id": 3, "is_booked": true, "seat": 4}
      ]
    }
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
