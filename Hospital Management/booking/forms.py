from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

        widgets = { 'booking_date' : DateInput(),}

        labels = {'p_name' : 'Patient Name:','p_phone' : "Patient Phone",'p_email' :"Patient Email" ,
                  'doc_name':"Doctor Name",'booking_date':"Booking Date"}
        
# Dr. Corrie T.M Anderson Pediatrician

# Dr. Naresh Trehan  Cardiologist

# Dr. Mohit Bhatt Neurologist

# Dr. Robert Sternberg  Psychologist

# Dr. David Bryant  Dermotologist