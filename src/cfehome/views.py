from django.http import HttpResponse; 


def home_page(request):
    return HttpResponse("hello StackCloud")