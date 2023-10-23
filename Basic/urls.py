from django.urls import path
from Basic.views import home  # Import the view

urlpatterns = [
    path('', home, name='home'),  # Map the root URL to the "home" view
    # Add more URL patterns as needed
]
