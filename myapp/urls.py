
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
rt=DefaultRouter()

rt.register('',views.UserViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
# path('list/',views.ListAp.as_view()),
    # path('',views.req),
    # path('',include(rt.urls)),
    path('forgot/',views.Forgot.as_view()),
    path('reset/',views.Reset.as_view()),
    path('register2/',views.RegisterAPI.as_view()),
    path('',views.TestApi.as_view()),
    path('login2/',views.Loginuser.as_view()),
    path('update_pass/',views.UpdatePass.as_view()),
    path('tokenLogin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
