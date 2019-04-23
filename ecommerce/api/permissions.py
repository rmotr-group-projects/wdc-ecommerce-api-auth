from rest_framework import permissions
from api.models import APIClient


class IsNotHacker(permissions.BasePermission):

    # view level permission
    def has_permission(self, request, view):
        # check if the user name contains the word "hacker". If so, return Flase.
        # Otherwise, return True.

        # The name that you need to evaluate is taken from `request.user.username`
        # in case it is a regular User, or from `request.user.name` in case it
        # is an APIClient.
        if isinstance(request.user, APIClient):
            username = request.user.name 
        else:
            username = request.user.username
        if 'hacker' in username.lower():
            return False
        else:
            return True


class IsOddProductID(permissions.BasePermission):

    # object level permission
    def has_object_permission(self, request, view, obj):
        # check if the product id is an odd integer. If so, returns True.
        # Otherwise return False.
        product = obj
        if product.id % 2 == 0:
            return False
        return True
