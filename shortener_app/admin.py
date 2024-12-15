from django.contrib import admin
from .models import URLShortener, AliasedURL  # Import both models

# Register the models so they appear in the admin panel
admin.site.register(URLShortener)
admin.site.register(AliasedURL)
