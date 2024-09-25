
from django.contrib import admin
from django.urls import path
from tests import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tests.urls", namespace="tests")),
]
