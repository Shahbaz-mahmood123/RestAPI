from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views

router = routers.DefaultRouter()
router.register(r'bugs', views.BugViewSet)
router.register(r'projects', views.ProjectViewset)
router.register(r'user', views.UserViewset)
router.register(r'enhancement', views.EnhancementViewset)
router.register(r'feature', views.FeatureViewset)
router.register(r'adduser', views.AddUserViewset)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
