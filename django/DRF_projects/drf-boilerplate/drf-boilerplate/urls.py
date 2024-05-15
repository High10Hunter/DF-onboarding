from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from students.urls import students_router
from modules.urls import modules_router
from users.urls import users_router

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.registry.extend(users_router.registry)
router.registry.extend(modules_router.registry)
router.registry.extend(students_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "api/v1/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/v1/", include(router.urls)),
    # Swagger
    path(
        "docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
