from portalvagas.vagas.models import Vaga, Candidatura
from portalvagas.candidatos.models import Candidato


def criar_candidatura(request):
    vaga_id = request.POST.get("vagas")
    vaga = Vaga.objects.get(id=vaga_id)

    candidato, _ = Candidato.objects.get_or_create(
        email=request.POST.get("email"),
        defaults={
            "nome": request.POST.get("nome"),
            "data_nascimento": request.POST.get("data_nascimento"),
            "experiencia": request.POST.get("experiencia"),
        }
    )

    _, created = Candidatura.objects.get_or_create(
        candidato=candidato,
        vaga=vaga,
    )

    return created
