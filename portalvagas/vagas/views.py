from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from portalvagas.vagas.forms import CandidaturaForm
from portalvagas.vagas.facade import criar_candidatura


def candidatar(request):
    form = CandidaturaForm()
    if request.method == "POST":
        form = CandidaturaForm(request.POST)

        if form.is_valid():
            candidatura_criada = criar_candidatura(request)

            if candidatura_criada:
                messages.success(request, "Candidatura registrada com sucesso!")
            else:
                messages.warning(request, "Você já se candidatou a esta vaga.")

            return redirect("vagas:candidatar")

    return render(request, "vagas/candidatar.html", {"form": form})
