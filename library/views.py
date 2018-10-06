from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from library.models import Student, Book
from rest_framework import viewsets
from library.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Create your views here.

def showlogin(request):
    return render(request, 'public/login.html')

def showregister(request):
    return render(request, 'public/register.html')

def registeruser(request):
    data = request.POST

    username,password,gender,country = data['username'], data['password'],data['gender'],data['country']
    s = Student(username=username, password=password, gender=gender, country=country)
    s.save()

    if s.id:
        # successful insert inside the database table
        return HttpResponseRedirect(reverse('library:login-page'))
    else:
        return HttpResponse('Error in registration')

def authenticateuser(request):
    data = request.POST
    username, password = data['username'], data['password']

    sl = Student.objects.filter(username=username, password=password)
    if len(sl):
        # session (logged in user specific from a machine)
        # store multiple data in the session
        request.session['loggedinusername'] = username # remember the username at django server for the user session
        request.session['loggedinuserid'] = sl[0].id

        return HttpResponseRedirect(reverse('library:home-page'))
    else:
        return HttpResponseRedirect(reverse('library:login-page'))

def showhome(request):
    if 'loggedinusername' not in request.session:
        return HttpResponseRedirect(reverse('library:login-page'))

    booklist = Book.objects.all()
    studentid = request.session['loggedinuserid']

    for book in booklist:
        book.isbookissued = len(book.student_set.filter(pk=studentid)) > 0

        if book.noofcopies:
            issuedcount = book.student_set.count()
            copieslefttoissue = book.noofcopies - issuedcount
            book.cannotissue = copieslefttoissue == 0
        else:
            book.cannotissue = True

    return render(request, 'private/home.html', {
        'booklist': booklist,
        'username': request.session['loggedinusername'], #access the remembered data from the session
        'studentId': request.session['loggedinuserid']
    })

def issuebook(request, bookId):
    studentId = request.session['loggedinuserid']

    student = Student.objects.get(pk=studentId)
    book = Book.objects.get(pk=bookId)

    student.booksissued.add(book)

    student.save()

    return HttpResponseRedirect(reverse('library:home-page'))

def returnbook(request, bookId):
    book = Book.objects.get(pk=bookId)
    studentid = request.session['loggedinuserid']

    book.student_set.remove(studentid)

    return HttpResponseRedirect(reverse('library:home-page'))

def showbook(request, bookId):
    if 'loggedinusername' not in request.session:
        return HttpResponseRedirect(reverse('library:login-page'))

    book = Book.objects.get(pk=bookId)
    return render(request, 'private/show-book.html', {
        'book': book,
        'username': request.session['loggedinusername'] # access the remembered data from the session
    })

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('library:login-page'))
