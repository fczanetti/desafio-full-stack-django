import pandas as pd
from django.shortcuts import render
from django.db.models import Count

from datetime import date
from portalvagas.vagas.models import Vaga
from portalvagas.candidatos.models import Candidato


def dashboard(request):
    vagas_df = pd.DataFrame(list(Vaga.objects.values("status")))
    vagas_status = vagas_df["status"].value_counts().to_dict() if not vagas_df.empty else {}

    candidatos_por_vaga = (
        Vaga.objects.annotate(num_candidatos=Count("candidatos"))
        .values("titulo", "num_candidatos")
    )
    candidatos_df = pd.DataFrame(candidatos_por_vaga)
    candidatos_dict = (
        dict(zip(candidatos_df["titulo"], candidatos_df["num_candidatos"]))
        if not candidatos_df.empty
        else {}
    )

    candidatos = Candidato.objects.all()
    hoje = date.today()
    idades = [
        (hoje.year - c.data_nascimento.year) -
        ((hoje.month, hoje.day) < (c.data_nascimento.month, c.data_nascimento.day))
        for c in candidatos
    ]
    idade_media = round(sum(idades) / len(idades), 1) if idades else 0

    vagas_abertas = Vaga.objects.filter(status=Vaga.ABERTA).values("setor")
    setor_df = pd.DataFrame(vagas_abertas)
    setor_top = setor_df["setor"].value_counts().idxmax() if not setor_df.empty else None

    context = {
        "vagas_status": vagas_status,
        "candidatos_dict": candidatos_dict,
        "idade_media": idade_media,
        "setor_top": setor_top,
    }
    return render(request, "dashboard/dashboard.html", context)
