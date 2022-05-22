from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from urllib.parse import urlencode
from django.views import View
from django.contrib.auth import logout as log_out
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Site/home.html')

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)