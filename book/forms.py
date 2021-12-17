from django import forms

class SearchForm(forms.Form):
    keyward = forms.CharField()