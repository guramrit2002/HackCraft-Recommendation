from django.urls import path
from .views import hackathonpost,hackathonget


urlpatterns = [
    path('post',hackathonpost),
    path('get',hackathonget)
]
