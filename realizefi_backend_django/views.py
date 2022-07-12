from django.utils.decorators import classonlymethod
from rest_framework import generics
from rest_framework.viewsets import ViewSetMixin


class SingleResourceViewSet(ViewSetMixin, generics.GenericAPIView):
    METHOD_TO_ACTION = {
        'retrieve': 'get',
        'partial_update': 'patch',
        'destroy': 'delete',
        'update': 'put',
        'post': 'create'
    }

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        class_methods = set(dir(cls))
        if not actions:
            actions = {}
            for action, method in cls.METHOD_TO_ACTION.items():
                if action in class_methods:
                    actions[method] = action

        return super().as_view(actions, **initkwargs)  # noqa
