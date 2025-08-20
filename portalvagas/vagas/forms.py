from django import forms

from portalvagas.candidatos.models import Candidato


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "experiencia": forms.Textarea(attrs={"class": "form-control"}),
        }
