from django.shortcuts import render
from Three_Seconds_Passwords.forms import UserForm,UserProfileInfoForm

#imports for views
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse  # Changed from django.core.urlresolvers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):

    return render(request,'Three_Seconds_Passwords/index.html')

def register(request):
    
    registered = False
    #check for the post method then assign to a variable
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        #check for valid
        if user_form.is_valid() and profile_form.is_valid():
            #we tell the form to save it in the model
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #working on the profile
            profile = profile_form.save(commit=False)
            profile.user = user
            #check if they is a file in the request.
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, 'Three_Seconds_Passwords/register.html',{'registered':registered,
                                                        'user_form':user_form,
                                                        'profile_form':profile_form})

def user_login(request):
    #request method

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #using authenticate from django to authenticate the user

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("someone treid to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'Three_Seconds_Passwords/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice" )