from django import forms
from .models import Message

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your message here...', 'class': 'w-full px-3 py-2 border rounded-md' }),
        }