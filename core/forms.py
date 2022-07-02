from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        fields = ('finish','title',)
        model = Note