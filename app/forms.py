from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField


class RegisterForm(UserCreationForm):
  pass

class RecaptchaForm(forms.Form):
  Recaptcha = ReCaptchaField()


