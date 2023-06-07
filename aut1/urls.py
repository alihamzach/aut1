from django.contrib import admin
from django.urls import path, include
from rest_auth.views import LoginView, LogoutView
from rest_auth.registration.views import SocialLoginView

from api.views import GoogleLogin, FacebookLogin

# Other URL patterns in your project

urlpatterns = [
    # Other URL patterns in your project
    path('admin/', admin.site.urls),
    # Login and Logout
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),

    # Signup
    path('api/registration/', include('rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    # Facebook Login
    path('api/facebook/login/', FacebookLogin.as_view()),

    # Google Login
    path('api/google/login/', GoogleLogin.as_view()),


    # Other URL patterns in your project
]