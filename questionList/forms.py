from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """
        As we have needed only 4 fields hence we are creation our own 
        form by inheriting the Default UserCreationForm
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']