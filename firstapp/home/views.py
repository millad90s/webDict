from django.http import HttpResponse
from django.shortcuts import render
from ip3country import CountryLookup


# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World Django')


def browser_info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    return render(request, 'browser_info.html', {'browser_name': user_agent})


def ip_user(request):
    user_info = request.META.get('REMOTE_ADDR')
    return render(request, 'browser_info.html', {'browser_ip': user_info})


def show_info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_ip = request.META.get('REMOTE_ADDR')
    # user_ip = '159.146.73.217'
    lookup = CountryLookup()
    country_code = lookup.lookupStr(user_ip)
    data = {
        'browser_name': user_agent, 'user_ip': user_ip, 'country_code': country_code,
    }

    return render(request, 'browser_info.html', data)
