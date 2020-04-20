from django.shortcuts import render, redirect
from .models import Destination, Reviews, Cart, Reviews
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from Hrishikesh.settings import EMAIL_HOST_USER

def home(request):

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests':dests})

def about(request):
    return render(request,'about.html')

def credits(request):
    return render(request,'credits.html')

def aboutme(request):
    return render(request,'aboutme.html')

def destinations(request,name):

    des_details = Destination.objects.get(name=name)

    print(name)
    
    reviews = Review.objects.filter(destination=name).values('review','heading','name')
 

    print(reviews)

    if request.user.is_authenticated:
        return render(request,'destination.html',{'dest':des_details , 'reviews':reviews, 'length' : len(reviews)})

    else:
        return redirect('login')



def cart(request,price,name):

    
        
    current_user = request.user

    print(current_user)

    cart = Cart.objects.get(username=current_user)

    cart.cart += price
    cart.destination = name

    print(cart)

    Cart.objects.filter(username=current_user).update(cart=cart.cart,destination=cart.destination)

    print(cart)

    messages.info(request,'Added to Cart succesfully')
        
    return redirect('/')
    
def search(request):

    if request.method == 'POST':
        city = request.POST['city']
        budget = request.POST['budget']

        dest = Destination.objects.get(name=city)
        price =  Destination.objects.filter(name=city).values('price')

        print(budget)

        budget = int(budget)

        print(dest.price)   

    if dest.price > budget:
        return render(request,'tooless.html')

    else:
        return render(request,'search.html',{'destination':dest,'budget':budget})

    return redirect('/')


def delete_cart(request):

    user = request.user

    cart = Cart.objects.get(username=user)

    cart.cart = 0 

    Cart.objects.filter(username=user).update(cart=cart.cart)

    return redirect('/')

def show_cart(request):

    current_user = request.user

    cart = Cart.objects.get(username=current_user)

    dest = Destination.objects.get(name=cart.destination)

    return render(request,'cart.html',{'cart':cart,'dest':dest})


def review(request,name):

    if request.method == "POST":
        heading = request.POST['heading']
        review = request.POST['review']
        destination = name
        user = request.user

        print(heading)
        print(review)
        print(name)

        Reviews.objects.create(name=user,destination=destination,review=review,heading=heading)

        des_details = Destination.objects.get(name=name)
    
        reviews = Reviews.objects.filter(destination=name).values('review','heading','name')
 

        return render(request,'destination.html',{'dest':des_details , 'reviews':reviews, 'length' : len(reviews)})

    elif request.method == 'GET':
        heading = request.GET.get('heading',False)
        review = request.GET.get('review',False)
        destination = name
        user = request.user

        print(heading)
        print(review)
        print(name)

        Reviews.objects.create(name=user,destination=destination,heading=heading,review=review)

        des_details = Destination.objects.get(name=name)
    
        reviews = Reviews.objects.filter(destination=name).values('review','heading','name')
 

        return render(request,'destination.html',{'dest':des_details , 'reviews':reviews, 'length' : len(reviews)})
    
    else:
        print('H')

    return redirect('/')




def email(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            email = request.POST['email']

            email = [email]

            print(email)

            send_mail(
                'WELCOME TO TRAVELLO!!',
                'WELCOME TO TRAVELLO!!We hope u like every moment of your experience here !!',
                EMAIL_HOST_USER,
                email
            )

    else:
        return redirect('login')
        

    return redirect('/')

def checkout(request):
    return render(request,'checkout.html')