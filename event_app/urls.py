from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('organization', views.OrganizationViewSet)
router.register('event', views.EventViewSet)
urlpatterns = router.urls