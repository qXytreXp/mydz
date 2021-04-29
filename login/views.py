from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError


class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user == None:
            return render(request, 'signin.html', {'errors': {'Користувача немає'}})
        login(request, user)

        return redirect('/')


class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        errors = set()
        
        first_name = request.POST['first_name'].replace(' ', '')
        last_name = request.POST['last_name'].replace(' ', '')
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        if not first_name or first_name.isspace():
            errors.add('Поле імені не має бути пустим')

        if not last_name or last_name.isspace():
            errors.add('Поле прізвища не має бути пустим')

        if not email or email.isspace():
            errors.add('Поле e-mail не має бути пустим')
        
        if len(password) < 8 and password:
            errors.add('Пароль не має бути меньше 8 символів')
        
        if not password or password.isspace():
            errors.add('Пароль не має бути пустим')

        if password != repeat_password:
            errors.add('Паролі не збігаються')

        if not errors:
            try:
                user = User.objects.create_user(
                    username=first_name+last_name,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()

                return redirect('login:signin')
            except IntegrityError:
                errors.add('Такий email уже використовується')

        return render(request, 'signup.html', context={'errors': errors})


def logout_user(request):
    logout(request)

    return redirect('/')