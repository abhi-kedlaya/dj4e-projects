from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def myview(request):
    num_visits = request.session.get('num_visits', 0)+1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])

    print(request.COOKIES)
    oldval = request.COOKIES.get('gaul', None)
    resp = HttpResponse('In this view - the gaul cookie value is ' + str(oldval) + ' view count='+str(num_visits))
    if oldval :
        resp.set_cookie('gaul', int(oldval)+1) #No expired date = until browser close
    else :
        resp.set_cookie('gaul', 325) #No expired date = until browser close
    resp.set_cookie('asterix', 300, max_age=90) # seconds until expiry
    resp.set_cookie('dj4e_cookie', '276441f6', max_age=1000)

    return resp
