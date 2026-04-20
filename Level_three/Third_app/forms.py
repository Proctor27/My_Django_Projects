from django import forms
from django.core import validators

#custom validator to make sure the first letter must be Z
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("it needs to start with a Z")

class Form_Cupid(forms.Form):
    name = forms.CharField()  #validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

"""def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Stupid Bot!')
        return botcatcher"""