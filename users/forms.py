from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


ROLE_CHOICES = (
    ('Viewer', 'Viewer'),
    ('Scraper', 'Scraper')
)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","role")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if self.cleaned_data['role'] == 'Scraper':
                scraper = Group.objects.get(name=self.cleaned_data['role']) 
                user.groups.add(scraper)
            else:
                viewer = Group.objects.get(name="Viewer") 
                user.groups.add(viewer)
        
        return user