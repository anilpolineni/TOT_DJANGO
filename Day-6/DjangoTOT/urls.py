"""DjangoTOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home),
    path('abt/',views.abt),
    path('myname/<name>/',views.myname),

    path('table/<int:num>',views.table),
    path('names/<name>/<int:age>',views.names),

    path('login/',views.login,name="login"),

    path('register/',views.register,name="register"),

    path('js/',views.script,name="js"),


    path('operations/',views.operations,name="operations"),

    path('operators/',views.operators,name="operators"),
    path('ar/',views.arthe,name="arthe"),


    path('',include('app2.urls'))

]
