from django.urls import include, path
from msgservice import views


SERVICE_LIST = views.MsgServiceViewSet.as_view({
    'post' : 'register_service',
    'get'  : 'users'
})

urlpatterns = [
    path(r'register/', views.MsgServiceViewSet.as_view(
        {'post': 'register_service'},name='user_register'
    )),
    path(r'userlist/', views.MsgServiceViewSet.as_view(
        {'get': 'users'},name='list_users'
    )),
]