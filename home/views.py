from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "home/homepage.html"


class IntroductionView(TemplateView):
    template_name = "home/../templates/our_story.html"

