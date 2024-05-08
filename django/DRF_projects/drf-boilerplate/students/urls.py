from rest_framework.routers import SimpleRouter
from .views import StudentsApiView

students_router = SimpleRouter()
students_router.register(r"students", StudentsApiView, basename="students")
