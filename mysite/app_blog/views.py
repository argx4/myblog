from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView # type: ignore


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context=None)
