from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . models import Pet,CartItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . forms import signupform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
# Create your views here.
def list_pets(request):
    object_list=Pet.objects.all()
    return render(request,'petsapp/list.html',{'object_list':object_list})
def pet_detail(r,id):
    idd=Pet.objects.get(id=id)
    return render(r,'petsapp/petdetail.html',{'data':idd})

def register(request):
    if request.method=='POST':
        fn=signupform(request.POST)
        if fn.is_valid():
         fn.save()
    else:
        fn=signupform()
    return render(request,'petsapp/signUp.html',{'form':fn})

def user_login(request):
    if request.method=='POST':
        fn=AuthenticationForm(request=request,data=request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password']
            u=authenticate(username=uname,password=upass) # not print the password
            print(u)
            # print(uname)
            # print(upass)
            if u is not None:
                login(request,u)
                return redirect('/pets')
                # return render(request,'petsapp/petdetail.html')
        
    else:
        fn=AuthenticationForm()
    return render(request,'petsapp/login.html',{'form':fn})
def user_profile(r):
    return render(r,'petsapp/profile.html')
def user_logout(request):
    logout(request)
    return redirect('/login')

# for seaching in database
def search_results(request):
    query = request.GET.get('query', '')
    # Perform the database search based on the query
    pets = Pet.objects.filter(name__icontains=query)
    if len(query) == 0:
      messages.error(request,"No search result found .please refine your query")
      pets=Pet.objects.none()
      
    return render(request, 'petsapp/search_results.html', {'query': query, 'pets': pets})




# def home(request):
#     pets = Pet.objects.all()
#     return render(request, 'petsapp/home.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'petsapp/petdetail.html', {'pet': pet})

def add_to_cart(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    cart_item, created = CartItem.objects.get_or_create(pet=pet)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def update_cart(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    cart_item = CartItem.objects.get(pet=pet)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()

    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'petsapp/cart.html', {'cart_items': cart_items})

def checkout(request):
    # You can implement payment gateways or other order processing logic here
    # For simplicity, we'll just clear the cart and display a success page

    if request.method == 'POST':
        # Process the payment here (not implemented for simplicity)
        # After successful payment processing, you can update order status, generate invoice, etc.
        # For now, we'll just clear the cart and display a success page
        CartItem.objects.all().delete()
        return render(request, 'petsapp/checkout_success.html')

    # If the request is not POST (e.g., GET request), render the checkout page
    return render(request, 'petsapp/checkout.html')















