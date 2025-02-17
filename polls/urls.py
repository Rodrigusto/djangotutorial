from django.conf import settings
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls

from . import views



app_name = "polls"
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
] + debug_toolbar_urls()
