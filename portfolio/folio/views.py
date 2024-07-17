from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact


def contact(request):
    # success = False
    if request.method == "POST":
        print("post")
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        content = request.POST.get("content")
        print(name, email, number, content)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(
                request,
                "Length of name should be greater than 2 and less than 30 words ",
            )
            return render(request, "home.html")

        if len(email) > 1 and len(email) < 30:
            pass
        else:
            messages.error(request, "invalid email try again ")
            return render(request, "home.html")
        print(len(number))
        if len(number) > 9 and len(number) < 13:
            pass
        else:
            messages.error(request, "invalid number please try again ")
            return render(request, "home.html")
        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(
            request, "Thank You for contacting me!! Your message has been saved "
        )
        print("data has been saved to database")
        request.session['form_submitted'] = True
        return redirect('/')
    success = request.session.pop('form_submitted', False)
    return render(request, "home.html", {'success': success})

