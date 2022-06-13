from myapp.custompermission import mypermission
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
# from rest_framework.permissions import (IsAuthenticated, 
#                                         IsAdminUser, 
#                                         IsAuthenticatedOrReadOnly, 
#                                         DjangoModelPermissions,
#                                         DjangoModelPermissionsOrAnonReadOnly)

# Create your views here.
class Studentclass(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [mypermission]