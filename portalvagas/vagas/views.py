from django.shortcuts import render


def candidatar(request):
    return render(request, "vagas/candidatar.html")
