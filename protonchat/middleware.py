from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Forces login for all pages except:
    - LOGIN_URL
    - REGISTER_URLS
    - STATIC/MEDIA URLs
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Allowed paths without login
        allowed_paths = {
            reverse('login'),
            reverse('register'),
        }

        # If user not logged in and requesting a protected page → redirect
        if (not request.user.is_authenticated
            and request.path not in allowed_paths
            and not request.path.startswith(settings.STATIC_URL)
            and not request.path.startswith(settings.MEDIA_URL)):

            return redirect('login')

        return self.get_response(request)
