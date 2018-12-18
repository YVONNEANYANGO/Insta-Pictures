from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class Comment(forms.Form):
    name = forms.CharField(label='Comments' ,max_length=30)
    
    