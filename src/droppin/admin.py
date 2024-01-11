from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your visitor-admin class here.
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cus_name', 'cus_email', 'cus_pass','date_created')
    search_fields = ('cus_name', 'cus_email', 'cus_pass','date_created')
    ordering = ('cus_name', 'cus_email', 'cus_pass','date_created')
    list_filter = ('cus_name', 'cus_email', 'cus_pass','date_created')

admin.site.register(Customer, CustomerAdmin)


# Register your order-admin class here.
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date', 'date_created')
    search_fields = ('cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date', 'date_created')
    ordering = ('cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date', 'date_created')
    list_filter = ('cli_name', 'cli_email', 'cli_address', 'cli_city', 'cli_phone', 'cli_subj', 'cli_qty', 'cli_date', 'date_created')

admin.site.register(Order, OrderAdmin)


# Register your visitor-admin class here.
class ContactorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email_contactor', 'mess_contactor','date_created')
    search_fields = ('email_contactor', 'mess_contactor','date_created')
    ordering = ('email_contactor', 'mess_contactor','date_created')
    list_filter = ('email_contactor', 'mess_contactor','date_created')

admin.site.register(Contactor, ContactorAdmin)


# Register your visitor-admin class here.
class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('post_id', 'author_post', 'category_post', 'title_post', 'description_post', 'rated_post', 'capacity_post','date_created')
    search_fields = ('post_id', 'author_post', 'category_post', 'title_post', 'description_post', 'rated_post', 'capacity_post','date_created')
    ordering = ('post_id', 'author_post', 'category_post', 'title_post', 'description_post', 'rated_post', 'capacity_post','date_created')
    list_filter = ('post_id', 'author_post', 'category_post', 'title_post', 'description_post', 'rated_post', 'capacity_post','date_created')

admin.site.register(Post, PostAdmin)


# Register your visitor-admin class here.
class CommentorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time', 'date_created')
    search_fields = ('cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time', 'date_created')
    ordering = ('cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time', 'date_created')
    list_filter = ('cmt_id', 'cmt_name', 'cmt_address', 'cmt_description', 'cmt_time', 'date_created')

admin.site.register(Commentor, CommentorAdmin)




#Interface admin django customized
admin.site.site_header = ("NEATLAND")
admin.site.site_title = ("By NEAT IT CORP")
admin.site.index_title = ("NEATLAND Database")
