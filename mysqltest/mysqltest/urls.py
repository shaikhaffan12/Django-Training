from django.contrib import admin
from django.urls import path,include
from myapp.views import posthere
from myapp.views import updatehere

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addData',posthere,name='addData'),
    path('upData/<int:pk>',updatehere,name='upData'),
]
