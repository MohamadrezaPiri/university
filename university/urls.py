from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('students', views.StudentViewset)

urlpatterns = router.urls

