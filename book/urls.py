from django import urls
from . import views

app_name="book"

urlpatterns = [
    urls.path("search/", views.QueryView, name="app_entry"),
]