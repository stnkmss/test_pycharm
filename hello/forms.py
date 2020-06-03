from django import forms


class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
    # name = forms.CharField(label='name')
    # mail = forms.CharField(label='mail')
    # age = forms.IntegerField(label='age')
