from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render
from django.http import HttpRequest
from django.forms import modelformset_factory
from .models import Client
from .forms import ClientForm
from django.contrib.auth.models import User


@login_required
def index(request: HttpRequest):
    clients_form_set = modelformset_factory(Client,
                                            form=ClientForm,
                                            fields=('status',),
                                            widgets='',
                                            extra=0)
    context = {
        'clients_form': clients_form_set(queryset=Client.objects.filter(
            response_person__in=[request.user.id]
        ).prefetch_related(Prefetch('response_person',
                                    queryset=User.objects.all(
                                    ).only('first_name',
                                           'last_name'
                                           ).select_related('userprofile')
                                    )
                           )
                                         )
    }
    if request.method == "POST":
        formset = clients_form_set(
            request.POST,
            request.FILES,
        )
        if formset.is_valid():
            formset.save()
    return render(request, 'clients/list_clients.html', context)
