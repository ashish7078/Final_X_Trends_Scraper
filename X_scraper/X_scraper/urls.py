from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("trends_scraper.urls")),  # all API endpoints
]

# React fallback for frontend (catch-all, but exclude static/assets)
urlpatterns += [
    re_path(r"^(?!static/|assets/).*", TemplateView.as_view(template_name="index.html")),
]
