from django import forms


class NewMessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(),
                           required=True)
