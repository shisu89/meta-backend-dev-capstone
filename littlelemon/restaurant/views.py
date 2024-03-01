from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# def home(request):
#     return render(request, 'home.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')