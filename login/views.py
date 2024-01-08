from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from signup.models import EmployeeDetails
from leaves.models import Leave
from django.contrib.auth.models import User
# Create your views here.

# views.py

def loginAction(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            employee_details = EmployeeDetails.objects.get(user = user)
            user_type = employee_details.user_type
            user_created= User.objects.get(username=user)
            request.session['user_details'] = {
                'username': user_created.username
            }
            print(user_type)
            if user_type == 'employee':
                return redirect('employee_dashboard')
            elif user_type == 'manager':
                return redirect('manager_dashboard')

    return render(request, 'login_page.html')

def employeAction(request):
    if request.user.is_authenticated:
        # Fetch leaves data for the logged-in employee
        user_details = request.session.get('user_details', {})
        user_email = user_details.get('username', '')
        print(user_email)
        user_created= User.objects.get(username=user_email)
        user = User.objects.get(username=user_email)
        print(user)
        leaves_data = Leave.objects.filter(user=user)
        # Pass leaves_data to the template context
        print(leaves_data)
        return render(request, 'employee_dashboard.html', {'leaves_data': leaves_data})
    else:
        return render(request, 'login.html')

def managerAction(request):
    return render(request, 'manager_dashboard.html')