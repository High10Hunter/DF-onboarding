from rest_framework.routers import SimpleRouter
from .views import SignUpApiView

users_router = SimpleRouter()
users_router.register(r"users", SignUpApiView, basename="users")
