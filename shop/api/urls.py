
from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
