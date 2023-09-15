from rest_framework.routers import DefaultRouter
from .views import PersonDetailAPI, PersonAPI

router = DefaultRouter()

router.register('', PersonAPI, basename='person')
router.register('', PersonDetailAPI, basename='person')

urlpatterns = router.urls