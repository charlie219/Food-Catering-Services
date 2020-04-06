"""foodcatering URL Configuration

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
from django.urls import path
from foca import views
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.show),
    path('login/',LoginView.as_view()),
    path('customreg/',views.customreg),
    path('check/',views.check), 
	path('home/',views.home), 
	path('logoutview/',views.logoutview),
    path('sendmail/',views.sendmail),
    path('buy/<int:id>/<int:qnt>',views.buy),
    path('confirm/',views.confirm),
    path('send/',views.mail),
    path('cart/',views.cart),
    path('delete/',views.delete)
]
