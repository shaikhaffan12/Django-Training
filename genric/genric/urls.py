from django.contrib import admin
from django.urls import path
from GenericApp.views import StudentCreate, StudentDestroy, StudentList, StudentListCreate, StudentRetrieve, StudentRetrieveDestroy, StudentRetrieveUpdate, StudentUpdate, StudentRetrieveUpdateDestroy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulist/', StudentList.as_view(), name='StudentList' ),
    path('stucreate/', StudentCreate.as_view(), name='StudentCreate' ),
    path('sturet/<int:pk>', StudentRetrieve.as_view(), name='StudentRetrieve'),
    path('studes/<int:pk>', StudentDestroy.as_view(), name='StudentDestroy'),
    path('stuupdate/<int:pk>', StudentUpdate.as_view(), name='StudentUpdate'),
    path('stulstcr/', StudentListCreate.as_view(), name='StudentListCreate'),
    path('sturetup/<int:pk>', StudentRetrieveUpdate.as_view(), name='StudentRetrieveUpdate'),
    path('sturetdes/<int:pk>', StudentRetrieveDestroy.as_view(), name='StudentRetrieveDestroy'),
    path('sturetupdes/<int:pk>', StudentRetrieveUpdateDestroy.as_view(), name='StudentRetrieveUpdateDestroy'),
]
