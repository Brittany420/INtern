from django.shortcuts import render,redirect, get_object_or_404
# from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import auth

# from .models import User
from .models import E_account
from .models import User


# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')



def employer(request):


        if request.method=='POST':
            if request.POST['password_1']==request.POST['password_2']:
                try:
                    user=E_account.objects.get(employer_email=request.POST['employer_email'])

                    return render(request, 'accounts/employer.html', {'error':'Someone has already using that email address'})


                except E_account.DoesNotExist:
                    user=E_account.objects.create_user(

                    employer_email=request.POST['employer_name'],
                    employer_fname=request.POST['employer_fname'],
                    employer_lname=request.POST['employer_lname'],
                    company_name=request.POST['company_name'],

    #need company name here??????????
                #    employer_email=request.POST['employer_email'],
                    employer_password =request.POST.get('password_1'))

                    auth_login(request,user)
                    return redirect('employer_moreinfo')

            else:
                return render(request, 'accounts/employer.html', {'error1':'Passwords have to match!'})

        else:
            return render(request, 'accounts/employer.html')


#change username to email

def student(request):
    #here is the actual signup page for students
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['student_email'])
                return render(request, 'accounts/student.html', {'error':'Someone has already using that email'})

            except User.DoesNotExist:
                user=User.objects.create_user(
                    request.POST['student_email'],
                    password=request.POST['password1'],
                    First_name=request.POST['First_name'],
                    Last_name=request.POST['Last_name'])

                user.save()
                auth_login(request,user)
                return redirect('sboard')
                #return redirect('/accounts/' + str(s_account.id), s_account)
        else:
            return render(request, 'accounts/student.html', {'error':'Passwords must match!'})

    else:
        return render(request, 'accounts/student.html')
#
#
def employer_moreinfo(request):
    # account=get_object_or_404(User)

    return render(request, 'accounts/employer_moreinfo.html')



def sboard(request):
    # account=get_object_or_404(User)
    user = request.user

    return render(request, 'accounts/sboard.html')

def eboard(request):
        # account=get_object_or_404(User)


    return render(request, 'accounts/eboard.html')

# {'First_name': First_name}

# def student_moreinfo(request):
#     if request.method=='POST':
#         if request.POST['Biography'] and request.POST['info'] :
#             s_account=S_account()
#             s_account.Biography=request.POST['Biography']
#             s_account.info=request.POST['info']
#             s_account.hunter=request.user
#             s_account.save()
#             return redirect('/accounts/' + str(s_account.id), s_account)
#
#         else:
#             return render(request, 'accounts/student_moreinfo.html', {'error':'All fields are required!'})
#
#     else:
#
#         return render(request, 'accounts/student_moreinfo.html')





 # account=get_object_or_404(User)
 #    user = request.user
 #
 #    return render(request, 'accounts/create_s_profile.html',
 #        {'username':user.username,
 #        'last_name':user.last_name,
 #        'first_name':user.first_name,
 #        })



@login_required
def create_s_profile(request):

    #here is the actual signup page for students



    user = request.user


    return render(request, 'accounts/create_s_profile.html')
        # {'email':user.email,
        # 'last_name':user.last_name,
        # 'first_name':user.first_name,
        # })







def e_profile(request):
    return render(request, 'accounts/e_profile.html')



def s_profile(request):
    return render(request, 'accounts/s_profile.html')


def login(request):
    if request.method=='POST':
        auth.authenticate(username=request.POST['username'],password=reuqest.POST['password'])
        if user is not None:
            auth_login(request,user)

            return redirect('home')

        else:
            return render(request,'accounts/log-in.html',{'error':'username or password is incorrect'})

    else:
        return render(request,'accounts/log-in.html')

@login_required
def logout(request):
    if request.method=='POST':
        auth.logout(request)
    else:
        return redirect('home')
