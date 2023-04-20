from django import forms

from app.models import *

class TOPICFORM(forms.ModelForm):
    class Meta:
        model=TOPIC
        fields='__all__'

class WEBPAGEFORM(forms.ModelForm):
    class Meta:
        model=WEBPAGE
        fields='__all__'

class ACCESSFORM(forms.ModelForm):
    class Meta:
        model=ACCESSRECORDS
        fields='__all__'