from django.db.models import Count


menu = [{'title': "Создать тест", 'url_name': 'tests:addtest'},
        {'title': "Пройти тест", 'url_name': 'tests:test'},
]

auth = [{'title': "Войти", 'url_name': 'tests:login'},
        {'title': "Регистрация", 'url_name': 'tests:register'},
]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['auth'] = auth
        return context