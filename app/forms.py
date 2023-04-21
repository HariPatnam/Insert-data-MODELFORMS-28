from django import forms

from app.models import *

class TOPICFORM(forms.ModelForm):
    class Meta:
        model=TOPIC
        fields='__all__'

class WEBPAGEFORM(forms.ModelForm):
    class Meta:
        model=WEBPAGE
        #fields='__all__'
        #fields=['topic_name','name']
        exclude=['url']
        #widgets={'email':forms.PasswordInput,'url':forms.Textarea}
        labels={'topic_name':'TOPIC_NAME','name':'NAME','email':'EMAIL'}
        help_texts={'topic_name': '... WRITE UR GOVT NAME','name':'...WE CAN"T WRITE YOUR INSTA IDS','email':'..PSYCHO_SAI@GAMIL.COM  DON"T WRITE THESE TYPE OF IDS'}
        

class ACCESSFORM(forms.ModelForm):
    class Meta:
        model=ACCESSRECORDS
        fields='__all__'