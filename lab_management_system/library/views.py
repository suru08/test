from django.shortcuts import render, HttpResponse, redirect
from .models import admin_detailss, book_detailss
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def Admin_details(request):
    obj = admin_detailss.objects.first()
    context = {
        'datax': obj,
    }
    return render(request, 'index.html', context)


def save(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["pwd"]

        try:
            registered_user = admin_detailss.objects.get(email=email)
            messages.Success(request, 'No user with this email ID')
            return render(request, "Index.html")

        except admin_detailss.DoesNotExist:

            a = admin_detailss(name=name, email=email, password=password)
            a.save()

        if a:
            request.session["username"] = email
            return redirect("/login")
        else:
            return HttpResponse("registeration fail")


def login(request):
    if request.session.get("username") is not None:
        return render(request, "login.html")


def Admin_login(request):
    request.session["incorrect"] = ''
    if request.method == 'POST':

        input_email = request.POST['email']
        input_password = request.POST['pwd']

        try:
            registered_user = admin_detailss.objects.get(email=input_email)


            if input_password == registered_user.password:
                if request.session.get("incorrect") is not None:
                    if request.session.get("incorrect") is "1":
                        request.session["incorrect"] = "0"
                        request.session["loggedin_as"] = registered_user.name
                if request.session.get("loggedin_as") is not None:
                    data = book_detailss.objects.all()
                    return render(request, "admin_view.html", {'data': data})
            else:
                request.session["incorrect"] = "1"
                if request.session.get("incorrect") is not None:
                    return redirect("/login")
        except admin_detailss.DoesNotExist:
            messages.Success(request, 'No user with this email ID')


def Add_Book(request):
    if request.method == "POST":
        isbn1 = request.POST["ISBN"]
        book_name1 = request.POST["Book"]
        author_name1 = request.POST["Author"]
        category1 = request.POST["Category"]
        language1 = request.POST["Language"]

        b = book_detailss(isbn=isbn1, book_name=book_name1, author_name=author_name1, category=category1,
                          language=language1)
        b.save()
        data = book_detailss.objects.all()
        return render(request, "admin_view.html", {'data': data})


def delete_book(request):
    id = request.GET['id']
    book_detailss.objects.filter(book_id=id).delete()
    data = book_detailss.objects.all()
    return render(request, "admin_view.html", {'data': data})


def Update_Book(request):
    id = request.GET['id']
    if request.method == "POST":
        isbn1 = request.POST["ISBN"]
        book_name1 = request.POST["Book"]
        author_name1 = request.POST["Author"]
        category1 = request.POST["Category"]
        language1 = request.POST["Language"]

        book_detailss.objects.filter(book_id=id).update(isbn=isbn1, book_name=book_name1, author_name=author_name1,
                                                        category=category1, language=language1)
        data = book_detailss.objects.all()
        return render(request, "admin_view.html", {'data': data})