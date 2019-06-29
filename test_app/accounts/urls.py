from django.conf.urls import url

from accounts.views import UserRegistrationView

urlpatterns = [
    # User registration URL
    url(
        r'^register',
        UserRegistrationView.as_view(
            {'post': 'create'},
        ),
        name='user-registration',
    ),
]