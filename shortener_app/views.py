from django.shortcuts import redirect
from shortener_app.models import AliasedURL
from django.http import Http404

# Create your views here.
def redirect_view(req, alias):
    try:
        aliased_url = AliasedURL.objects.get(alias=alias)
        return redirect(aliased_url.url)
    except AliasedURL.DoesNotExist:
        raise(Http404('Aliased URL does not exist'))
