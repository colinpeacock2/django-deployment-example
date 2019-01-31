from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'text' : 'hello world', 'number':100}
    return render(request, 'app_one/index.html', context=my_dict)


def other(request):
    my_dict = {'insert_me' : 'OTHER'}
    return render(request, 'app_one/other.html', context=my_dict)


def relative(request):
    my_dict = {'insert_me' : 'RELATIVE URL'}
    return render(request, 'app_one/relative_url_templates.html', context=my_dict)