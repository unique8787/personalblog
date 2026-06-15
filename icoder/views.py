from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
def contact(request):
    return HttpResponse("This is the contact page")
def about(request):
    return HttpResponse("This is the about page")