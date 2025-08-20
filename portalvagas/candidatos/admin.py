from django.contrib import admin

from portalvagas.candidatos.models import Candidato


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento')
    search_fields = ('nome', 'email')
