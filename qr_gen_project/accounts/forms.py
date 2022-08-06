from .models import QRUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = QRUser
        fields = ('fullname', 'email', 'password1', 'password2')
        widgets = {
            'form_item': forms.TextInput(
                attrs={
                    'class': 'form-control', 'required': False
                }
            )
}


    # def clean(self):
    #     value = self.cleaned_data['fullname']
    #     if not value:
    #         return 'Name Empty'
    #     # Do some cleaning later
    #     return value

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user