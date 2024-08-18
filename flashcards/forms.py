from django import forms


class FlashcardForm(forms.Form):
    paragraph = forms.CharField(widget=forms.Textarea, label="Input Paragraph")
