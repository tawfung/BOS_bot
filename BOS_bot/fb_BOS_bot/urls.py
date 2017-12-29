from django.conf.urls import include, url
from .views import BOS_botView

urlpatterns = [
    url(r'^e3175d914a0fd91f8ef0250a55d32b04e0babe45d041ec29e5/?$', BOS_botView.as_view()),
]
