from django.urls import path
from portalvagas.vagas import views


app_name = "vagas"
urlpatterns = [
    path("", views.candidatar, name="candidatar")
]