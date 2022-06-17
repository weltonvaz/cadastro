from django.shortcuts import render, redirect
from core.engine.validate_form import is_valid, country_uf
from core.engine.commit import commit
from core.models import Enderecos


def index(request):
    stored_addresses = Enderecos.objects.all()
    context = {'stored_addresses': stored_addresses}
    return render(request, 'index.html', context)


def cadastro(request):
    form_fields = {'rua': '', 'bairro': '', 'cidade': '', 'estado': '', 'complemento': '', 'cep': ''}
    if str(request.method) == 'POST':
        inputted_data = request.POST
        for key, value in inputted_data.items():
            if key == 'rua':
                form_fields['rua'] = value
            elif key == 'bairro':
                form_fields['bairro'] = value
            elif key == 'cidade':
                form_fields['cidade'] = value
            elif key == 'uf':
                form_fields['estado'] = country_uf.get(value)
            elif key == 'complemento':
                form_fields['complemento'] = value
            elif key == 'cep':
                form_fields['cep'] = value

        if is_valid(form_fields):
            new_endereco = Enderecos(**form_fields)
            new_endereco.save()
            commit()
            request.method = 'GET'
            return redirect(index)
        else:
            request.method = 'GET'
            return render(request, 'cadastro.html')
    return render(request, 'cadastro.html')
