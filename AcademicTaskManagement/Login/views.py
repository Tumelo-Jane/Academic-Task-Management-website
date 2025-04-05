from django.shortcuts import render,redirect, get_object_or_404
from .models import login_details
from .models import signup_details
from .models import task
from django.http import HttpResponse
from datetime import date

def logIn_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            userLogin = login_details.objects.get(user=username, passw=password)
            request.session['username'] = username
            request.session['password'] = password

            return render(request, 'home/homepage.html', {'student': userLogin})
        
        except login_details.DoesNotExist:
            return render(request, 'home/login.html', {'error': 'Invalid email or password'})


    return render(request, 'home/login.html')

def signup_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']


        if password == confirmPassword:
            signupDetails = signup_details(name=name, surname=surname, username=username, password=password)
            signupDetails.save()
            login = login_details(user=username,passw=password,signUp_details=signupDetails)
            login.save()
            return render(request,'home/login.html', {'logSuccess': 'Sign up Successfull ,Please login'})
        else:
            return render(request,'home/signup.html', {'passwordErr': "Passwords don't match"})

    return render(request, 'home/signup.html')

def home_page(request):
    username = request.session.get('username')
    password = request.session.get('password')
    try:
        userLogin = login_details.objects.get(user=username, passw=password)
    except login_details.DoesNotExist:
        return redirect('../logIn_page')
    
    if userLogin:
        if request.method == 'POST':
            taskOptions = request.POST['taskOptions']
            taskTitle = request.POST['taskTitle']
            taskDueDate = request.POST['taskDueDate']
            taskDesc = request.POST['taskDesc']
            taskReminder = request.POST.get('taskReminder','off')
            
            signupDetails = userLogin.signUp_details

            taskDetails = task(taskType=taskOptions, taskTittle=taskTitle,subDate=taskDueDate, taskDesc=taskDesc, taskReminder=taskReminder,signUp_details=signupDetails)
            taskDetails.save()

            return render(request, 'home/homepage.html', {'student': userLogin,'taskCreated': 'Task Successfull created'})
        else:
            return render(request, 'home/homepage.html',{'student': userLogin})
    else:
        return redirect('../logIn_page')


def calender_page(request):
    username = request.session.get('username')
    password = request.session.get('password')
    today = date.today()
    try:
        userLogin = login_details.objects.get(user=username, passw=password)
    except login_details.DoesNotExist:
        return redirect('../logIn_page')
    
    if userLogin:
        signupDetails = userLogin.signUp_details
        tasks = task.objects.filter(signUp_details=signupDetails,subDate=today)

        return render(request, 'home/calender.html', {'tasks': tasks})

    return render(request, 'home/calender.html')

def delete_task(request, task_id):
    task_to_delete = get_object_or_404(task, id=task_id)
    username = request.session.get('username')
    password = request.session.get('password')
    today = date.today()
    try:
        userLogin = login_details.objects.get(user=username, passw=password)
    except login_details.DoesNotExist:
        return redirect('../logIn_page')
    task_to_delete.delete()

    if userLogin:
        signupDetails = userLogin.signUp_details
        tasks = task.objects.filter(signUp_details=signupDetails,subDate=today)

    
    return render(request, 'home/calender.html', {'student': userLogin,'tasks': tasks})


def logout(request):
    request.session.clear()
    return redirect('../logIn_page')