from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    STATUS_CHOICES = (
        (Client.Status.WORK, 'В работе'),
        (Client.Status.REJECT, 'Отказ'),
        (Client.Status.CLOSE, 'Сделка закрыта'),
        (Client.Status.NOT_WORK, 'Не в работе')
    )
    status = forms.ChoiceField(label='',
                               widget=forms.Select,
                               choices=STATUS_CHOICES)

    class Meta:
        model = Client
        fields = ('status',)
