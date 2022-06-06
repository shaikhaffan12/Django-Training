from django.urls import path, include
import serail1.views as view
urlpatterns = [
    path('', view.serilizeJson, name='serializeJSON'),
]
