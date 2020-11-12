from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label = "search")

class CreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs = {'id': 'title'}), required=True, max_length=30)
    create = forms.CharField(widget=forms.Textarea(attrs={'id': 'create'}), required=True)

class EditForm(forms.Form):
    edit = forms.CharField(widget=forms.Textarea(attrs={'id': 'create'}), required=True)