from django.contrib import admin
from .models import Booking,Departments,Doctors

# Register your models here.

#this class is created to show the items in tabular form and is passed to the model
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','boooked_on')

admin.site.register(Booking,BookingAdmin)

admin.site.register(Departments)
admin.site.register(Doctors)
