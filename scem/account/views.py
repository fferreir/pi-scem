from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserEditForm
from django.contrib import messages

@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard'}
    )

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        if user_form.is_valid() :
            user_form.save()
            messages.success(
                request,
                'Perfil usuáriao atualizado com sucesso'
            )
        else:
            messages.error(request, 'Erro ao atualizar o perfil')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(
            request,
            'account/edit.html',
            {
                'user_form': user_form,
            }
        )