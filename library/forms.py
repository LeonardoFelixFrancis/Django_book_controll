from django import forms
from .models import BookModel

GEEKS_CHOICES =(
    ("", ""),
    ("Yes", "Yes"),
    ("No", "No")
)
  

class BooksForm(forms.Form):
    book_name = forms.CharField()
    rating = forms.IntegerField(required=False)
    synopsis = forms.CharField(widget=forms.Textarea, required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False)
    start_reading = forms.ChoiceField(widget=forms.Select, choices=GEEKS_CHOICES, label="Started Reading", required=False)

    
class BooksFilterForm(forms.Form):
    book_name = forms.CharField(required=False, label="Book Name")
    rating_start = forms.IntegerField(required=False, label="Rating Start")
    rating_end = forms.IntegerField(required=False, label="Rating End")
    start_date_init = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False, label="Start Date - Start")
    start_date_end = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False, label="Start Date - End")
    end_date_init = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False, label="Finish Date - Start")
    end_date_end = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False, label="Finish Date - End")
    start_reading = forms.ChoiceField(widget=forms.Select, choices=GEEKS_CHOICES, label="Started Reading", required=False)