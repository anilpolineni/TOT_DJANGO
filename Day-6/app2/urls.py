from django.urls import path

from.views import (home,grid)

urlpatterns = [
	path('home/',home),
	path('grid/',grid),
	]