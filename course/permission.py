from rest_framework.permissions import BasePermission
from .models import Subscription


class IsPaid(BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        course_id = request.resolver_match.kwargs.get('course_id')
        subs = Subscription.objects.filter(user=request.user, subscription=course_id).first()
        return bool(subs)
