from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import AliasedURL

# Create your views here.

def redirect_view(request, alias):
    url_mapping = get_object_or_404(AliasedURL, alias = alias)
    return redirect(url_mapping.url)
