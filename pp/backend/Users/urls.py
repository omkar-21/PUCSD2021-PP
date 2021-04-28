from django.urls import include, path
from rest_framework import routers
from Users import views
from rest_framework.authtoken.views import ObtainAuthToken
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
LOGOUT = views.UserLogoutViewSet.as_view({
    'post' : 'logout_user',
})
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path(r'logout/', views.UserLogoutViewSet.as_view(
        {'post': 'logout_user'},name='logout'
    )),
]