from django.shortcuts import render
from django.views.generic import TemplateView
from .models import IceCream


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ice_cream_types = IceCream.objects.all()
        ice_cream_features = IceCream.objects.filter(featured=True)
        daily_ice_cream = IceCream.objects.filter(available='Daily')
        weekly_ice_cream = IceCream.objects.filter(available='Weekly')
        seasonal_ice_cream = IceCream.objects.filter(available='Seasonal')

        context = {
            'ice_cream_types': ice_cream_types,
            'ice_cream_features': ice_cream_features,
            'daily': daily_ice_cream,
            'weekly': weekly_ice_cream,
            'seasonal': seasonal_ice_cream,
        }

        return context
