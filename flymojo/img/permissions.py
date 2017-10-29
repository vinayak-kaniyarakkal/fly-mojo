import functools
from django.http import JsonResponse


class UserPassTest(object):

    def __init__(self, view):
        self.view = view

    def __call__(self, request, *args, **kwargs):
        res = self.validate(request)
        if res is None:
            return self.view(*args, **kwargs)
        else:
            return JsonResponse(res)

    def __get__(self, obj, type=None):
        return functools.partial(self, obj)

    def validate(request):
        if not request.user.is_authenticated():
            return {'success': False, 'details': 'Login required'}


class ModeratorRequired(UserPassTest):
    def validate(request):
        try:
            request.user.moderator_set.get()
        except:
            return {'success': False, 'details': 'Should be a moderator'}


class MerchantRequired(UserPassTest):
    def validate(request):
        try:
            request.user.merchant_set.get()
        except:
            return {'success': False, 'details': 'Should be a moderator'}
