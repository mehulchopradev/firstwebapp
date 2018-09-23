# from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    '''html = '<html><body><h2>Welcome to my first django app</h2><hr></body></html>'
    return HttpResponse(html)'''
    return render(request, 'welcome.html')

def contactus(request):
    '''html = '<html><body>U can reach us at 098790879087<br>Email: mehul@gmail.com</body></html>'
    return HttpResponse(html)'''

    # email and contact number are coming from a database
    email = 'mehul.chopra.dev@yahoo.com'
    mobile = '98870879087'
    addresses = ['India, 30/B Andheri', 'USA, Alabama', 'Brazil']
    return render(request, 'contactus.html', {
        'email': email,
        'mobile': mobile,
        'addresses': addresses
    })
