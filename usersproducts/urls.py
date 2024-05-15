"""
URL configuration for usersproducts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from apps.users.views import UserList, UserDetail
from apps.profiles.views import ProfileList, ProfileDetail
from apps.products.views import ProductList, ProductDetail
from apps.permissions.views import PermissionList, PermissionDetail, UserPermissionList
from apps.inventory.views import InventoryList, InventoryDetail
from apps.notifications.views import NotificationList, NotificationDetail
from apps.notifications.views import NotificationList, NotificationDetail
from apps.tickets.views import TicketList, TicketDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for the company",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product-detail'),
    path('permissions/', PermissionList.as_view(), name='permission-list'),
    path('permissions/<int:pk>/', PermissionDetail.as_view(),
         name='permission-detail'),
    path('user-permissions/', UserPermissionList.as_view(),
         name='user-permission-list'),
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(),
         name='notification-detail'),
    path('inventory/', InventoryList.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetail.as_view(), name='inventory-detail'),
    path('tickets/', TicketList.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),



]
