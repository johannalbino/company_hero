"""company_hero URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from employee.views import EmployeeView
from company.views import CompanyView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

docs_view = get_schema_view(
   openapi.Info(
      title="Company Hero API",
      default_version='v1',
      description="Documentação referente a API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="johann.albino.ti@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('funcionarios', EmployeeView, basename='funcionarios')
router.register('empresas', CompanyView, basename='empresas')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('api-docs/', docs_view.with_ui('redoc', cache_timeout=0), name='api-docs')
]
