from rest_framework import generics

from birthdays.models import Birthday
from .serializers import BirthdaySerializer

class AllBirthdays(generics.ListCreateAPIView):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer


class DetailBirthday(generics.RetrieveUpdateDestroyAPIView):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer

class ListUserBirthdays(generics.ListCreateAPIView):
    serializer_class = BirthdaySerializer
    def get_queryset(self):
        return Birthday.objects.filter(user=self.request.user)