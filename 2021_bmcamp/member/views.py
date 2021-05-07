from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
# Create your views here.
from .forms import RegistrationForm,AccountAuthenticationForm


def register_view(request,*args,**kwargs):
    user = request.user

    if user.is_authenticated:
        return redirect('transient')
        #return HttpResponse(f"You're already authenticated as {user.email}.")
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # after form.save() the defined 'clean' family function are execute
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email,password = raw_password)
            login(request,account)
            destination = get_redirect_if_exists(request)
            if destination: # if destination != None
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form


    return render(request,'register.html',context)

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect('home')

def login_view(request,*args,**kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('home')
            # email = request.POST['email']
            # password = request.POST['password']
            # user = authenticate(email=email,password=password)
            # if user:
            #     login(request,user)
            #     destination = get_redirect_if_exists(request)
            #     if destination:
            #         return redirect(destination)
            #     return redirect('home')
        else:
            context['login_form'] = form
    return render(request,'login.html',context)

def transient_view(request,*args,**kwargs):
    context = {}
    context['user'] = request.user
    return render(request,'transient.html',context)
def get_redirect_if_exists(request):
    redirect = None
    if request.GET: # if it's a get request
        if request.GET.get('next'): # if kwargs has 'next'
            redirect = str(request.GET.get('next'))
    return redirect