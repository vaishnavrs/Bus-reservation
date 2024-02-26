from django import forms
from tempus_dominus.widgets import DatePicker


class BusSearchForm(forms.Form):
    source=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    destination=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(widget=DatePicker(
        options={
            'format': 'YYYY-MM-DD',  # adjust the format as needed
            'showTodayButton': True,
        },
    ))