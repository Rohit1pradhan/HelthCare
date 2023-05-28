
from django.urls import path, include

from api import views

urlpatterns = [
    path('register/',views.register.as_view()),
    path('login/',views.login.as_view()),
    path('madicine/',views.madicine.as_view()),
    path('activation/',views.activation.as_view()),
    path('updateMedicianTiming/',views.updateMedicianTiming.as_view()),
    path('deleteMadicine/',views.deleteMedician.as_view()),

]