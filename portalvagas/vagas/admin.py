from django.contrib import admin

from portalvagas.vagas.models import Vaga, Candidatura


class CandidaturaInLine(admin.TabularInline):
    model = Candidatura
    extra = 1


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'setor', 'status', 'data_abertura')
    search_fields = ('titulo', 'setor')
    inlines = [CandidaturaInLine]


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'candidato__nome', 'vaga', 'data', 'status_candidatura')
    search_fields = ('candidato__nome', 'candidato__email', 'vaga__titulo')
