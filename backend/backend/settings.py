from pathlib import Path #new importsss
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b0j7wk+lfjt+n9u)8!oqm4(bcf_+xsv!mmrznxp5x=zeyv#_-9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

#new code
REST_FRAMEWORK = {
    # Specifies the default authentication mechanisms for the Django REST Framework.
    # In this case, it uses JWT (JSON Web Tokens) for authentication, provided by Simple JWT.
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    
    # Specifies the default permission classes for API views.
    # 'IsAuthenticated' ensures that only authenticated users can access the API endpoints.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    # Sets the lifetime of the access token.
    # This token is used to authenticate API requests.
    # It will expire after 30 minutes, requiring clients to either log in again or use a refresh token.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    
    # Sets the lifetime of the refresh token.
    # This token is used to obtain new access tokens when they expire.
    # It remains valid for 1 day, allowing clients to reauthenticate without providing their credentials again.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
#end of new code

# Application definition

INSTALLED_APPS = [
    # Default Django apps required for core functionality
    'django.contrib.admin',          # Admin panel for managing the database and site content.
    'django.contrib.auth',           # User authentication system (login, logout, permissions).
    'django.contrib.contenttypes',   # Framework for handling different content types.
    'django.contrib.sessions',       # Manages user sessions (storing data between requests).
    'django.contrib.messages',       # Messaging framework for flashing one-time messages to users.
    'django.contrib.staticfiles',    # Manages serving static files like CSS, JS, and images.

    # Custom app for the project
    "api",                           # Your custom app where API-related functionality is implemented.

    # Third-party libraries for added functionality
    "rest_framework",                # Django REST Framework for building and managing APIs.
    "corsheaders",                   # Middleware to handle Cross-Origin Resource Sharing (CORS) policies.
]


MIDDLEWARE = [
    # Security middleware that helps protect the site from common security threats
    'django.middleware.security.SecurityMiddleware',   # Provides security-related headers and protections (e.g., HTTPS redirection).
    # Middleware to handle user session management (preserves session data between requests)
    'django.contrib.sessions.middleware.SessionMiddleware',   # Manages sessions to store information across requests (e.g., user logged in).
    # Middleware that provides common view handling functionality
    'django.middleware.common.CommonMiddleware',   # Provides some common utilities like URL normalization and handling of 404 errors.
    # Middleware that provides Cross-Site Request Forgery (CSRF) protection
    'django.middleware.csrf.CsrfViewMiddleware',   # Ensures requests made by users are from trusted sources to prevent CSRF attacks.
    # Middleware to handle user authentication (manages user login and permission checking)
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # Associates the authenticated user with the request.
    # Middleware for handling and displaying messages to users (flash messages)
    'django.contrib.messages.middleware.MessageMiddleware',   # Handles one-time messages (e.g., success or error messages after form submission).
    # Middleware to prevent clickjacking attacks by setting an X-Frame-Options header
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Prevents the site from being embedded in iframes to protect against clickjacking.
    
    # CORS middleware to allow cross-origin requests from other domains (needed for APIs)
    "corsheaders.middleware.CorsMiddleware",   # Handles CORS (Cross-Origin Resource Sharing) headers, allowing your API to be accessed from different domains.
]


ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add the base directory where your project-level templates might be located
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,  # This is crucial - allows Django to find templates in each app's templates directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # Add debug to help diagnose template-related issues
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Database Configuration
# Uses PostgreSQL with credentials loaded from environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),  # Add this line
        'PASSWORD': os.getenv("DB_PWD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Allowing all origins (domains) to make cross-origin requests to the API
CORS_ALLOW_ALL_ORIGINS = True   # This allows any domain to access your API, which is useful in development but should be restricted in production to ensure security.

# Allowing credentials (cookies, HTTP authentication, etc.) to be included in cross-origin requests
CORS_ALLOW_ALL_CREDENTIALS = True   # This allows requests to include credentials (e.g., cookies, HTTP authentication), which can be necessary for maintaining user sessions across different domains.
