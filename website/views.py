from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client
from .forms import CreateAccountForm, SurveyForm
# Application Views


# Home Page
class LandingPage(TemplateView):
    template_name = 'website/landing_page.html'

class LoginPage(TemplateView):
    template_name = 'website/login_page.html'

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'website/home_page.html'

class CreateAccount(FormView):
    template_name = 'website/create_account.html'
    form_class = CreateAccountForm
    success_url = reverse_lazy('website:survey_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SurveyPage(LoginRequiredMixin, FormView):
    template_name = 'website/survey_page.html'
    form_class = SurveyForm
    success_url = reverse_lazy('website:home_page')

    def form_valid(self, form):
        client = Client.objects.get(user=self.request.user)
        data = form.cleaned_data
        client.first_priority = data['first_priority']
        client.second_priority = data['second_priority']
        client.third_priority = data['third_priority']
        client.save()
        return super().form_valid(form)
    
class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'website/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            "username": self.request.user.username
        }
        return context