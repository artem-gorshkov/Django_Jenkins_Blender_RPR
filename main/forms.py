from django import forms


class InputForm(forms.Form):
    Path = forms.CharField()
    RGB = forms.CharField()
