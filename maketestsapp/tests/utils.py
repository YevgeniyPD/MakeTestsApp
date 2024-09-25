from django.db.models import Count


menu = [{'title': "Создать тест", 'url_name': 'tests:addtest'},
        {'title': "Пройти тест", 'url_name': 'tests:tests'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context