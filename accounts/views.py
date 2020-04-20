from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from travello.models import Cart

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'invalid Credentials')
            return redirect('login')  

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():    
                
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email ID already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)

                user.save()

                cart = Cart.objects.create(username=username,cart=0,destination='Nowhere',quantity=1)
                cart.save()
                
                print('user created')
                return redirect('login')

                
        else:
           
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register2.html')

def logout(request):
    auth.logout(request)
    return redirect('/')