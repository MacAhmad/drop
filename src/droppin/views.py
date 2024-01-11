from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import CustomerForm, OrderForm, ContactorForm, PostForm, CommentorForm
from .models import *


# Create your store view here
def home(request):
    
    context = {"date":datetime.today()}
    return render(request, 'droppin/home.html', context)

# Create your cart view here
def booking(request):
    
    context = {"date":datetime.today()}
    return render(request, 'droppin/booking.html', context)


# Create your checkout view here
def actualities(request):
    
    customer = Customer.objects.all()
    count_cus = Customer.objects.all().count()
    
    post = Post.objects.all()
    count_post = Post.objects.all().count()
    
    order = Order.objects.all()
    count_order = Order.objects.all().count()
    
    commentor = Commentor.objects.all()
    count_cmt = Commentor.objects.all().count()
    
    paginator_post = Paginator(post, 3)
    page_post = request.GET.get('page_post')
    post = paginator_post.get_page(page_post)
    
    paginator_order = Paginator(order, 3)
    page_order = request.GET.get('page_post')
    order = paginator_order.get_page(page_order)
    
    paginator_commentor = Paginator(commentor, 3)
    page_commentor = request.GET.get('page_commentor')
    commentor = paginator_commentor.get_page(page_commentor)
    
    context = {"date":datetime.today(), "customer":customer, "count_cus":count_cus, "post":post, "count_post":count_post, "page_post":page_post, "paginator_post":paginator_post, "order":order, "count_order":count_order, "page_order":page_order, "paginator_order":paginator_order, "commentor":commentor, "count_cmt":count_cmt, "page_commentor":page_commentor, "paginator_commentor":paginator_commentor}
    return render(request, 'droppin/actualities.html', context)


# Create your immigration view here
def services(request):
    
    Order = ['cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date']
    if request.method == 'POST':
        # soumission de la form
        form_ord = OrderForm(request.POST or None)
        if form_ord.is_valid():
            form_ord.save()
            return redirect('home')
    else:
        # generation de la form initialement vide
        form_ord = OrderForm()
    
    context = {"date":datetime.today(), 'form_ord':form_ord}
    return render(request, 'droppin/services.html', context)


# Create your signall view here
def connect(request):
    
    Customer = ['cus_name', 'cus_email', 'cus_pass']
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context = {"date":datetime.today(), 'form':form}
    return render(request, 'droppin/connect.html', context)

# Create your signall view here
def signin(request):
    
    if request.method=='POST':
        cus_name = request.POST.get("cus_name")
        cus_pass = request.POST.get("cus_pass")
        
        user = authenticate(request, username=cus_name, password=cus_pass)
        
        if user is not None:
            login(request, user)
            username = user.username
            context = {'username':username}
            return render(request, 'droppin/home.html', context)
        
        else:
            messages.error(request, "Email ou Mot de passe erroné !")
            return redirect('/')
    
    context = {"date":datetime.today()}
    return render(request, 'droppin/signin.html', context)


# Create signout view.
def signout(request):
    logout(request)
    messages.success(request, "Vous vous êtes bien déconnecté !")
    return redirect('signin')


# Create your signall view here
def contact(request):
    
    Contactor = ['email_contactor', 'mess_contactor']
    form_ct = ContactorForm(request.POST or None)
    if form_ct.is_valid():
        form_ct.save()
        return redirect('actualities')
    else:
        # generation de la form initialement vide
        form_ct = ContactorForm()
        
    context = {"date":datetime.today(), 'form_ct':form_ct}
    return render(request, 'droppin/contact.html', context)


# Create your comment view here
def comment(request):
    
    Commentor = ['cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time']
    form_cmt = CommentorForm(request.POST or None)
    if form_cmt.is_valid():
        form_cmt.save()
        return redirect('actualities')
    else:
        # generation de la form initialement vide
        form_cmt = CommentorForm()
        
    context = {"date":datetime.today(), 'form_cmt':form_cmt}
    return render(request, 'droppin/comment.html', context)