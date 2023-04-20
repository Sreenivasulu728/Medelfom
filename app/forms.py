from django import forms
from app.models import *
class topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class webpagesform(forms.ModelForm):
    class Meta:
        model=Webpages
        fields='__all__'
    
class accessrecordsform(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
