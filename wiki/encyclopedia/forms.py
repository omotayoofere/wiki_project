from socket import fromshare
from django import forms



class NewEntryForm(forms.Form):
    title = forms.CharField(label='New Task')
    content = forms.CharField( widget=forms.Textarea )