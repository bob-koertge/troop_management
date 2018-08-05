from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.forms.utils import ValidationError
from bootstrap_datepicker_plus import DatePickerInput

from troop.models import (Scout, Parent, Leader,  User)


class LeaderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_leader = True
        if commit:
            user.save()
            Leader.objects.create(user=user)
        return user


class ParentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_parent = True
        if commit:
            user.save()
            Parent.objects.create(user=user)
        return user


class ScoutSignUpForm(UserCreationForm):
    dob = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_scout = True
        user.save()
        scout = Scout.objects.create(
            user=user,
            dob=self.cleaned_data.get('dob'),
        )
        return user
