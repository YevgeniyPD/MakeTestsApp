from django.db.models import Count


menu = [{'title': "Пройти тест", 'url_name': 'core:'},
        {'title': "Создать тест", 'url_name': 'core:'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context