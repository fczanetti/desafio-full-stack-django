from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from portalvagas.vagas.forms import CandidatoForm
from portalvagas.vagas.models import Vaga


def candidatar(request):
    form = CandidatoForm()
    vagas = Vaga.objects.filter(status='aberta')
    if request.method == "POST":

        vaga_id = request.POST.get("vaga")
        vaga = Vaga.objects.get(id=vaga_id)

        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save()
            candidato.vagas.add(vaga)
            messages.success(request, "Candidatura registrada com sucesso!")

            return redirect("vagas:candidatar")

    context = {"form": form, "vagas": vagas}
    return render(request, "vagas/candidatar.html", context)
