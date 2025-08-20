from django.urls import path
from portalvagas.dashboard import views


app_name = "dashboard"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
