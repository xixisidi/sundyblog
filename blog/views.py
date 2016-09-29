from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from models import *

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello myblog</h1>')
    
   
def article(request):
    articles = Article.objects.all()
    return render(request,"article.html",locals())








