from django import forms

from portalvagas.vagas.models import Vaga


class CandidaturaForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    experiencia = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "style": "height: 100px;"}),
        required=False
    )
    vagas = forms.ModelChoiceField(
        queryset=Vaga.objects.filter(status=Vaga.ABERTA),
        empty_label="Selecione uma vaga",
        widget=forms.Select(attrs={"class": "form-control"})
    )
