from django.db import models
from django.contrib.auth.models import User

# Create your customer model
class Customer(models.Model):
    cus_name = models.CharField(max_length=200, null=True)
    cus_email = models.CharField(max_length=200, null=True)
    cus_pass = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cus_name
    
    class Meta:
        ordering = ['-date_created']
        
        
# Create your order model
class Order(models.Model):
    cli_name = models.CharField(max_length=200, null=True)
    cli_email = models.CharField(max_length=200, null=True)
    cli_address = models.CharField(max_length=200, null=True)
    cli_city = models.CharField(max_length=200, null=True)
    cli_phone = models.CharField(max_length=200, null=True)
    cli_subj = models.CharField(max_length=200, null=True)
    cli_qty = models.CharField(max_length=200, null=True)
    cli_date = models.DateTimeField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cli_name
    
    class Meta:
        ordering = ['-date_created']
        
        
# Create your contactor model
class Contactor(models.Model):
    email_contactor = models.CharField(max_length=200, null=True)
    mess_contactor = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email_contactor
    
    class Meta:
        ordering = ['-date_created']
        
        
# Create your besoin model.
class Post(models.Model):
    
    CHOIX = (
        ('Graphics_Design', 'Graphics_Design'),
        ('Web_Design', 'Web_Design'),
        ('Marketing_Digital', 'Marketing_Digital'),
        ('Transformation_Digitale', 'Transformation_Digitale'),
        ('Video_Surveillance', 'Video_Surveillance'),
    )
    CHOICES = (
        ('40%', '40%'),
        ('75%', '75%'),
        ('80%', '80%'),
        ('85%', '85%'),
        ('95%', '95%'),
        ('100%', '100%'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.AutoField(primary_key=True, unique=True, null=False)
    author_post = models.ForeignKey('Customer', related_name='customer', on_delete=models.CASCADE)
    category_post = models.CharField(max_length=200, choices = CHOIX)
    title_post = models.CharField(max_length=200, null=True)
    description_post = models.CharField(max_length=200, null=True)
    rated_post = models.CharField(max_length=200, null=True)
    capacity_post = models.CharField(max_length=200, choices = CHOICES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title_post
    
    class Meta:
        ordering = ['-date_created']
        
        
# Create your commentor model
class Commentor(models.Model):
    cmt_id = models.AutoField(primary_key=True, unique=True, null=False)
    cmt_name = models.CharField(max_length=200, null=True)
    cmt_address = models.CharField(max_length=200, null=True)
    cmt_description = models.CharField(max_length=200, null=True)
    cmt_time = models.DateTimeField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cmt_name
    
    class Meta:
        ordering = ['-date_created']