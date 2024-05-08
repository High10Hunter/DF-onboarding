from rest_framework.routers import SimpleRouter
from .views import ModulesApiView

modules_router = SimpleRouter()
modules_router.register(r"modules", ModulesApiView, basename="modules")
