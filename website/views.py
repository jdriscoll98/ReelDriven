from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Application Views


# Home Page
class LandingPage(TemplateView):
    template_name = 'website/landing_page.html'

class LoginPage(TemplateView):
    template_name = 'website/login_page.html'

class CreateAccount(FormView):
    template_name = 'website/create_account.html'
    form_class = ClientForm

class HomePage(TemplateView):
    template_name = 'website/home_page.html'
