from django import forms

class SearchForm(forms.Form):
    data = forms.CharField(label='Team name', max_length=500)
