"""
Definition of views.
"""

from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
import pyodbc
from app.models import registerAlt


def ConnectSql(request):
    conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=LAPTOP-K1SQILB0;'
                     'Database=Altours;'
                     'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('select * from registerAlt')
    result = cursor.fetchall()
    return render(request,'app/layout.html',{'registerAlt':result})

def layout(request):
    if request.method == 'POST':
        #email request.POST['email']
        #password request.POST['password']
        #print(email,password)
        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LeLdo0fAAAAAF11jduD0MkGKCR_w6zZllkbrjsz'
        capthchaData ={
            'secret':secretKey,
            'response':clientKey
            }
        r =requests.Post('https://www.google.com/recaptcha/api/siteverify ,data=capthchaData')
        response =json,loads(r.text)
        verify = response['success']
        print('your success is:',verify)
        if verify:
           return HttpResponse('<script> alert("success");</script>')
    else:
           return HttpResponse('<script> alert(" not success");</script>')
    return render(request,'app/layout.html')

       

def SaveData(request):
    if request.method == 'POST':
        conn = pyodbc.connect('Driver={SQL Server};'    
                      'Server=LAPTOP-K1SQILB0;'
                      'Database=Altours;'
                      'Trusted_Connection=yes;')
        form = registerAlt(request.POST)
        a=registerAlt()
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')
        a.password_confirmation = request.POST.get('password_confirmation')
        cursor = conn.cursor()
        cursor.execute("EXEC usp_insertdata @email='"+a.email+"',@password='"+a.password+"',@password_confirmation='"+a.password_confirmation+"'")
        cursor.commit()
        return ConnectSql(request)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(      
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        } 
    )

def goa(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(      
        request,
        'app/goa.html',
        {
            'title':'goa',
            'year':datetime.now().year,
        } 
    )

def goahotels(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(      
        request,
        'app/goahotels.html',
        {
            'title':'goa',
            'year':datetime.now().year,
        } 
    )

def hotelbooking(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(      
        request,
        'app/hotelbooking.html',
        {
            'title':'goa',
            'year':datetime.now().year,
        } 
    )

def destination(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/destination.html',
        {
            'title':'Destination',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def holiday(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render( 
        request,
        'app/holiday.html',
        {
            'title':'Holiday',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def family(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/family.html',
        {
            'title':'lehladakh',
            'message':'Your application description page.',   
            'year':datetime.now().year,
        }
    )

def honeymoon(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/honeymoon.html',
        {
            'title':'Honeymoon',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def hotels(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/hotels.html',
        {
            'title':'Hotels',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def amritsar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/amritsar.html',
        {
            'title':'amritsar',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def lehladakh(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/lehladakh.html',
        {
            'title':'lehladakh',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def odisha(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/odisha.html',
        {
            'title':'odisha',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def gangtok(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gangtok.html',
        {
            'title':'gangtok',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def jaipur(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/jaipur.html',
        {
            'title':'jaipur',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def MadhyaPradesh(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MadhyaPradesh.html',
        {
            'title':'Madhaya Pradesh',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def kashmir(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kashmir.html',
        {
            'title':'kashmir',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def hampi(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render( 
        request,
        'app/hampi.html',
        {
            'title':'hampi',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def shimla(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render( 
        request,
        'app/shimla.html',
        {
            'title':'shimla',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def mathura(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render( 
        request,
        'app/mathura.html',
        {
            'title':'mathura',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
