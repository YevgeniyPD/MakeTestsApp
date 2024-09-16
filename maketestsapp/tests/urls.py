from django.urls import path
from .views import *
from . import views
app_name = "core"
urlpatterns = [path("", hometestsapp.as_view(), name="home"),
               path('add_test/', AddTest.as_view(), name='addtest'),
               path('test/', Test.as_view(), name='test'),
               path('login/', LoginUser.as_view(), name='login'),
               # path('logout/', logout_user, name='logout'),
               path('register/', RegisterUser.as_view(), name='register'),
               ]