from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts', views.PostViewSet)

app_name = "diary"
urlpatterns = [
  path("", views.index, name="index"),
  path("api/", include(router.urls)),
]
