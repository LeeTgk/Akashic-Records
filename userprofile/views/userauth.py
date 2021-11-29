from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect

from .forms import UserCreationForm, UserChangeForm

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'userprofile/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        messages.add_message(self.request, messages.SUCCESS, f"Registrado com sucesso.")

        login(self.request, user, "django.contrib.auth.backend.ModelBackend")

        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Erro ao se registrar.")

        return super().form_invalid(form)

class UserChangeView(UpdateView):
    form_class = UserChangeForm
    template_name = 'userprofile/change.html'
    success_url = reverse_lazy('change')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Erro ao alterar o usuario.")
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user