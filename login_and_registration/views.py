from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    template_name = "login_and_registration/registration.html"
    success_url = "/login/?registration_completed"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    pass


class Logout(View):
    pass
