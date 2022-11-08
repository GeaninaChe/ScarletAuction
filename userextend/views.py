from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages

from django.shortcuts import redirect, render
from django.views.generic import CreateView

# from ScarletAuction.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm


    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save()

            details_user = {
                'full_name': new_user,
                'username': new_user.username
            }
            # subject = 'Created a new account!'
            # message = get_template('userextend/mail_create_new_user.html').render(details_user)
            # from_email = EMAIL_HOST_USER
            # email_to = [new_user.email]
            #
            # email = EmailMessage(subject, message, from_email, email_to)
            # email.content_subtype = 'html'  # main content is now text/html
            # email.send()

        return redirect('homepage')

class AuthenticationNewForm(AuthenticationForm):
    template_name = 'userextend/login.html'
    model = UserExtend
    form_class = UserExtendForm

    def login_request(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                email_address = form.cleaned_data.get('email_address')
                password = form.cleaned_data.get('password')
                user = authenticate(email_address=email_address, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f'You are now logged in as {email_address}.')
                    return redirect('homepage')
                else:
                    messages.error(request, 'Invalid email or password.')
            else:
                messages.error(request, 'Invalid email or password.')
        form = AuthenticationForm()
        return render(request=request, template_name='registration/login.html', context={'login_form': form})




