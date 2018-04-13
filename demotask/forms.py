from django.forms import ModelForm

from demotask.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'emailid', 'message']