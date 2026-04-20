from django import forms
from first_app.models import Details

class MyNewForm(forms.ModelForm):
    # If you wanted to add custom validation or extra fields, they'd go here
    
    class Meta:
        model = Details  # Must be lowercase 'model'
        fields = '__all__' # Correctly includes all fields from the Details model