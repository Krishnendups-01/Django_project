from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
#    return HttpResponse("Welcome")
     products = product.objects.all().order_by('name')
     cat = Category.objects.all()
     context={
          'Product':products,
          'cat':cat,
     }
     # products = product.objects.filter(name='shoes')
     # products = product.objects.filter(rate= 5000)
     # products = product.objects.get(id=3)
     # print(products.images.url)
     # products = product.objects.filter(name='shoes').first()
     # products = product.objects.filter(category__name='Laptops')
     # for i in products:
     # print(products)
     return render(request,'home.html', context)
def categories(request):
     cat = Category.objects.all()
     return render(request,'categories.html',{'cat':cat})
     

def products(request):
     products= product.objects.all().order_by('name')
     return render(request,'products.html',{'Product':products})

def prods(request,id):
     products= product.objects.filter(category__id=id)
     # print(products)
     return render(request,'cat_prods.html',{'Product':products})

def productdetails(request,id):
     products= product.objects.get(id=id)
     return render(request,'prod_details.html',{'Product':products})


def signup(request):
     if request.method=="POST":
     #    name=request.POST['name']
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']

     #    print(name,username,password)
        user=User.objects.create_user(username,email,password)
        user.save()

     return render(request,'signup.html')

def loginpage(request):
     if request.method == "POST":
          username=request.POST.get('email')
          password=request.POST.get('password')
          
          user = authenticate(username=username,password=password)
          if user is not None:
               login(request,user)
               
               # return redirect('cart')
               if user.is_superuser:
                    return redirect('adminview')  
               else:
                     return redirect('home')
          else:
               messages.error(request,"Invalid Credentials!")
               return redirect('login')
     return render(request,'login.html')  

def logout(request):
     logout(request)
     return redirect('home')   

def addtocart(request,id):
     # if request.user.is_authenticated:
     #       products = get_object_or_404(product, id=id)
     #       Cart.objects.create(user=request.user, Product=products)
     #       return redirect('cart')
     # else:
     #    return redirect('login')
     if request.user.is_authenticated:
          Product = product.objects.get(id=id)
          user=request.user 
          # price=Product.rate
          # items,created =Cart.objects.get_or_create(user=user,Product=Product )
          try:
             cartitem = Cart.objects.get(user=user,Product=Product )
             cartitem.quantity +=1
          except Cart.DoesNotExist:
               cartitem = Cart.objects.create(user=user,Product=Product, quantity=1)
          # if cartitem:
          #      messages.error(request,'The product is already exist')
          # else:
          #     items=Cart.objects.create(user=user,product=Product,quantity=1,price=price)
          # total=sum(item.quantity*item.Product.rate for item in items) 
          # print(total)
     #      if not created:
     #           items.quantity +=1
     #      items.save()
          cartitem.save()
          return redirect('carts')     
     else:
          return redirect('login')
    

def cartpage(request):
     if request.user.is_authenticated:
          cartitems = Cart.objects.filter(user=request.user)  
          total=sum(item.quantity * item.Product.rate for item in cartitems) 
          return render(request, 'cart.html',{'cartprod':cartitems,'total':total})
          # print(total)
          # return render(request, 'cart.html',{'cartprod':cartitems}) 
          # both={
          #      'cartprod':cartitems,
          #      'total':total
          # }
          # return render(request, 'cart.html', both)
     else:
          return redirect('login')
     
     
def remove(request, id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(user=request.user, id=id) 
        cart_item.delete()
        return redirect('carts')
    else:
        return redirect('login')
       
def placeorder(request):
     cart_item = Cart.objects.filter(user=request.user)   
     if not cart_item.exists():
          return redirect ('products')
     existing_order = Order.objects.filter(user=request.user).first()
     if request.method == 'POST':
          address=request.POST.get('address')
          if existing_order:
               existing_order.address=address
               existing_order.save()
          else:
               order = Order.objects.create(user=request.user, address=address)
          

          return redirect('order_confirmation') 
     return render(request,'placeorder.html',{
          'cart_item':cart_item,
          'user': request.user,
          'existing_address': existing_order.address if existing_order else ''
     })

def orderconfirmation(request):
     return render(request,'order_confirmation.html')     

def create_product(request):
     if request.method =='POST':
          form = Productform(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect('home')
     else:
          form = Productform()
     return render(request,'create_product.html',{'forms':form})


def create_category(request):
     if request.method =='POST':
          form = Categoryform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')
     else:
          form = Categoryform()
     return render(request,'create_category.html',{'form':form})

def adminview(request):
     return render(request,'admin.html')

def editbyuser(request,getid):
     products = product.objects.get(id=getid)
     if request.method =='POST':
          products.name= request.POST['name']
          products.rate= request.POST['rate']
          products.description = request.POST['description']
          if 'image' in request.FILES:
               image=request.FILES['image']
          product.save()
          
          return redirect('product.html')
     return render(request,'edit.html',{'products':products})     



def deletebyuser(request,getid):
     products = product.objects.get(id=getid)
     
     if request.method =='POST':
          products.delete()

          return redirect('products')
     return redirect('product.html',{'products':products})

# def editbyuser(request,id):
#      edit= product.objects.get(id=id)
#      form= Productform(request.POST, request.FILES)
#      if request.method =='POST':
#           if 'image' in request.FILES:
#                image=request.FILES['image']
#           name= request.POST['name']
#           rate= request.POST['rate']
#           description = request.POST['description']
          
#           if edit:
#                edit.image=image
#                edit.name=name
#                edit.description=description
#                edit.rate=rate
#                edit.save()
#                return redirect('product.html')
#           else:
#                form = Productform
#      return render(request,'edit.html',{'form':form,'edit':edit})  