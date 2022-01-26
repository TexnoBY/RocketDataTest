from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from staff.permissions import IsYou
from .models import Employer
from .serializers import EmployerSerializer


class CommonView(generics.ListAPIView):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    permission_classes = (IsAdminUser,)


class LevelView(generics.ListAPIView):
    serializer_class = EmployerSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        level = self.kwargs['level']
        queryset = Employer.objects.filter(level=level)
        return queryset

class MeView(generics.ListAPIView):
    serializer_class = EmployerSerializer
    permission_classes = (IsYou,)

    def get_queryset(self):
        queryset = Employer.objects.filter(username=self.request.user.username)
        return queryset
