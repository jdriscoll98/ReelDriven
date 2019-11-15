from django.conf.urls import url

from .views import *

# Application Routes (URLs)


app_name = "website"

urlpatterns = [
    # Home Page
    url(r"^$", LandingPage.as_view(), name="landing_page"),
    url(r"^login$", LoginPage.as_view(), name="login"),
    url(r"^create$", CreateAccount.as_view(), name="create_account"),
    url(r"^home$", HomePage.as_view(), name="home_page"),
]
