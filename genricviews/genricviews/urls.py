from django.contrib import admin
from django.urls import path, include
# import GenericApp
from myapp.views import My_Student, My_StudentCreate, My_StudentDelete, My_StudentRetrieve, My_StudentUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getstudent/',My_Student.as_view(), name='getstudent'),
    path('createstudent/',My_StudentCreate.as_view(), name='createstudent'),
    path('retstudent/<int:pk>/',My_StudentRetrieve.as_view(), name='retrivestudent'),
    path('updatestudent/<int:pk>/',My_StudentUpdate.as_view(), name='updatestudent'),
    path('deletestudent/<int:pk>/',My_StudentDelete.as_view(), name='deletestudent'),
    # path('gen/', include('GenericApp.urls'))
]
