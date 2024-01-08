from django.shortcuts import render
from .models import * 
# import sqlite3 as sql
# fn=''
# ln=''
# emp=''
# em=''
# pwd=''

# Create your views here.
def signupAction(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        empcode = request.POST['empc']
        em = request.POST['email']
        pwd = request.POST['pwd']
        mn = request.POST['designation']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            employee = EmployeeDetails.objects.create(user=user, empcode=empcode, designation=mn, user_type=mn.lower())
            error = "no"
        except:
            error = "yes"

    return render(request, 'signup_page.html', locals())