
from django.http import HttpResponse

def home_page(request):
    print("home page requested")
    friends =[
        'ankit',
        'ravi',
        'uttm',
    ]
    return HttpResponse(friends,safe =False)
