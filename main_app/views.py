from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')
