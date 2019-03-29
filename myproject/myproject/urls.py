"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import include, path
# from . import views

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from myapp import views



# router = DefaultRouter()
# router.register(r'music', views.MusicViewSet)

# router = DefaultRouter()
# router.register('api/', views.LeadListCreate)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index),
    path('', include('myapp.urls')),
    path('', include('frontend.urls')),
    # path('api/', include(router.urls))
]

# urlpatterns += [
#     # your integrate path
#     url('', FrontendRenderView.as_view(), name='home')
# ]
# django no longer handles 404/403/500 errors; frontend does

