from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm, CustomUserCreationForm
# Create your views here.
def signupoptions(request):
    return render(request,'account/register_option.html')
def loadTemplate(request):
    if request.method=='POST':
        reg_type=request.POST['registration_type']
        if reg_type=='Police':
            return render(request,'account/signup_next_police.html')
        elif reg_type=='Hospital':
            return render(request,'account/signup_next_hospital.html')
        else:
            user_form = CustomUserCreationForm()
            customer_form = CustomerForm()
    # return render(request, 'account/register_user.html', {'user_form': user_form,
    #                                        'customer_form': customer_form})
            return render(request,'account/register_user.html',{'user_form': user_form,'customer_form': customer_form})
def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save(commit=False)
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer.user = user
            customer.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    # else:
    #     user_form = CustomUserCreationForm()
    #     customer_form = CustomerForm()
    # return render(request, 'account/register_user.html', {'user_form': user_form,
    #                                        'customer_form': customer_form})
def profile(request):
    return render(request, 'account/profile.html')
def logout(request):
    return render(request,'index.html')
    