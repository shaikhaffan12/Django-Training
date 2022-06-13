from django.contrib import admin
from django.urls import path,include
from myapp import views
from modelview import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()

# route.register('stuapi', views.Studentclass, basename='StudentApi')

route.register('stuapi', views.modelview, basename='StudentApi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
