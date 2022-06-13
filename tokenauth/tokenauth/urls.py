from django.contrib import admin
from django.urls import path,include
from myapp import views
# from Studentclass import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

route = DefaultRouter()

route.register('stuapi', views.Studentclass, basename='StudentApi')

# route.register('stuapi', views.modelview, basename='StudentApi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken', obtain_auth_token)
]
