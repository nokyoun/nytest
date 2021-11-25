import json
from django.contrib.auth import authenticate, forms, login, logout
from django.http import HttpResponse, request
from django.shortcuts import redirect, render

from templates.decorator import admin_only, unauthenticated_user
from django.contrib.auth.models import Group

#import authentication
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registerPage(request):
    print("sign up")
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            print(group)
            
            print('saved')
            messages.success(request,'Account was created for '+ username)
            return redirect('signup')
        else:
            print('not save')
    context = {'form':form}
    return render(request, 'authentication/signup.html', context)


def signup(request):
    print("log in")
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('login success')
            return redirect('home')
        else:
           print('incorrect')
           messages.info(request,'Username or password is incorrect')
                        
    context = {}
    return render(request, 'authentication/signin.html', context)



def logoutUser(request):
    logout(request)
    print('logout')
    return redirect('home')


def store(request):
    #wake
    products = Product.objects.filter(brand_id=2)
    context = {'products':products}
    return render(request, 'store/store.html', context)

def store2(request):
    #jew4u
    products = Product.objects.filter(brand_id=1)
    context = {'products':products}
    return render(request, 'store/store2.html', context)

def store3(request):
    #bhunyawat
    products = Product.objects.filter(brand_id=4)
    context = {'products':products}
    return render(request, 'store/store3.html', context)

def home(request):
    count = Product.objects.filter().count()
    print('home', count)
    n = count - 9
    last_ten = Product.objects.filter()[n:count]
    last_ten_in_ascending_order = reversed(last_ten)
    context = {'products':last_ten_in_ascending_order}
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')


def showItem(request):
    pData = json.loads(request.body)
    productId = pData['productId']
    action = pData['action']

    print('action', action)
    print('productID:', productId)

    return JsonResponse('get ID', safe=False)


@admin_only
def manage(request):
    if request.method == 'POST':
        prod = Product()
        
        print('db')

        #prod.brand = request.POST['pBrand']
        prod.name = request.POST.get('pName')
        prod.detail = request.POST.get('pDetail')
        prod.price = request.POST.get('pPrice')
        if len(request.FILES) !=0:
            prod.image = request.FILES['pFile']
        
        prod.save()
       
        print('inserted to db')
        messages.success(request,'Product was added ')
        return redirect('manage')

    return render(request, 'store/managePage.html')


def custPage(request):
    return render(request, 'store/custPage.html')

def preorder(request):
   
    return render(request, 'store/preorder.html')
