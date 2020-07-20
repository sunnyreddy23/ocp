from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

#from crm.users.api.views import UserViewSet
from preferences.views import TopicViewSet, PreferenceViewSet, MediumViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

#router.register("users", UserViewSet)
router.register("topic", TopicViewSet)
router.register("preference", PreferenceViewSet)
router.register("medium", MediumViewSet)


app_name = "api"
urlpatterns = router.urls