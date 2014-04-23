from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class DatasetsView(TemplateView):
    template_name = 'datasets.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'