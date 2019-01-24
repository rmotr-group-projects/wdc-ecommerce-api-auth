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

        return False


class IsOddProductID(permissions.BasePermission):

    # object level permission
    def has_object_permission(self, request, view, obj):
        # check if the product id is and odd integer. If so, returns True.
        # Otherwise return False.

        return False
