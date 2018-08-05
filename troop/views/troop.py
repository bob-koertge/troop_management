from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_parent:
            return redirect('parents:landing')
        if request.user.is_scout:
            return redirect('scouts:landing')
        if request.user.is_leader:
            return redirect('leaders:landing')

    return render(request, 'troop/home.html')
