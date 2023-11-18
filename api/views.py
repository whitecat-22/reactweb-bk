from rest_framework import viewsets
from .models import User, Customer, Project
from .serializers import UserSerializer, CustomerSerializer, ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.alive()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.alive()
    serializer_class = CustomerSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.alive()
    serializer_class = ProjectSerializer
