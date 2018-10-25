from django.shortcuts import render, redirect
from .models import User
import datetime


# Create your views here.

def index(request):
    email = request.COOKIES.get("Email")
    if not email:
        return render(request, "moyuweb/index.html", {})
    user = User.objects.get(Email=email)
    print(user.Nickname)
    return render(request, "moyuweb/index.html", {"Nickname": user.Nickname})


def login(request):
    context = {}
    context["title"] = "login"
    return render(request, "moyuweb/login.html", context)


def login_auth(request):
    context = {}
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        r_msg = User.Login(User, email, password)
        if r_msg == True:
            context = {
                "success_msg": "you succeed in login"
            }
            res = redirect("/moyuweb")
            current_time = datetime.datetime.utcnow()
            current_data = current_time + datetime.timedelta(seconds=60 * 60 * 24 * 7)
            # u = User.objects.get(Email=email)
            # res.set_cookie("Nickname",u.Nickname)
            res.set_cookie("Email", email, expires=current_data)
            return res
        else:
            context = {
                "error_msg": "email or password is wrong"
            }
    else:
        context = {
            "error_msg": "post no message"
        }
    return render(request, "moyuweb/login.html", context)


def logout(request):
    res = redirect("/moyuweb")
    res.delete_cookie("Email")
    return res


def issue(request):
    context = {}
    context["title"] = "issue"
    return render(request, "moyuweb/issue.html", context)


def me_sale(request):
    context = {}
    context["title"] = "me_sale"
    return render(request, "moyuweb/me_sale.html", context)


def me_transaction(request):
    context = {}
    context["title"] = "me_transaction"
    return render(request, "moyuweb/me_transaction.html", context)
