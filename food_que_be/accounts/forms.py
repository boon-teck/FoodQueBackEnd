from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterNormalUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
                'username', 'email',
                'password1', 'password2'
                ]

class RegisterTaskerUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
                'username', 'email',
                'password1', 'password2'
                ]

    def save(self, commit=True):
            user = super().save(commit=False)
            user.is_tasker = True
    
            if commit:
                user.save()
            return user