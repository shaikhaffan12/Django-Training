from django.urls import URLPattern, path
from GenericApp.views import StudentList

URLPattern = [
    path('stulist/', StudentList.as_view(), name='StudentList' )
]