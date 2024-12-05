from django.contrib import admin  # Import the admin interface for managing the Django project
from django.urls import path, include  # Import the 'path' and 'include' functions to define URL patterns
from api.views import CreateUserView  # Import the 'CreateUserView' class from your 'api' app views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Import views for handling JWT authentication

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface route: Accessible at /admin/
    path('api/user/register/', CreateUserView.as_view(), name="register"),  # Register new user route: Accessible at /api/user/register/
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),  # Token obtain route: Accessible at /api/token for getting access token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),  # Token refresh route: Accessible at /api/token/refresh to refresh the token
    path("api-auth/", include("rest_framework.urls")),  # API authentication routes: Include default routes for browsable API authentication
    path("api/", include("api.urls")),
]
