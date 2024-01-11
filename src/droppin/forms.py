from turtle import textinput
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Customer, Order, Contactor, Post, Commentor


# Register your visitor-form class here.
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['cus_name', 'cus_email', 'cus_pass']
        
        
# Register your order-form class here.
class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date']
        
        
# Register your visitor-form class here.
class ContactorForm(forms.ModelForm):
    
    class Meta:
        model = Contactor
        fields = ['email_contactor', 'mess_contactor']


# Register your visitor-form class here.
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['post_id', 'author_post', 'category_post', 'title_post', 'description_post', 'rated_post', 'capacity_post']
        
        
# Register your commentor-form class here.
class CommentorForm(forms.ModelForm):
    
    class Meta:
        model = Commentor
        fields = ['cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time']
        
        