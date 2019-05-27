from django.core.exceptions import ValidationError
from rest_framework import exceptions, permissions, authentication

from api.models import APIClient


def validate_authkey(value):
    """Raises a ValidationError if value has not length 32"""
    if not len(value) == 32:
        raise ValidationError(
            'Value must be a string containing 32 alphanumeric characters')


class APIClientAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        # Get the accesskey from the query parameters, and the secretkey from
        # the request headers.
        accesskey = request.query_params.get('accesskey')
        secretkey = request.META.get('secretkey')

        # Validate that AK and SK were given
        if not accesskey or not secretkey:
            return None

        # Validate that AK and SK are valids
        for key in [accesskey, secretkey]:
            try:
                validate_authkey(key)
            except ValidationError:
                raise exceptions.AuthenticationFailed('Invalid APIClient credentials')

        # Validate that APIClient exists for given AK and SK.
        # If it exists and it's active, return a tuple of (api_client, None).
        # Second element in the tuple means that there weren't errors.

        # If APIClient doesn't exist or is inactive, raise an AuthenticationFailed

        ### YOUR CODE HERE
        try:
            api_client = APIClient.objects.get(accesskey=accesskey, secretkey=secretkey)
            if api_client.is_active:
                return (api_client, None)
            else:
                raise api_client.DoesNotExist
        except APIClient.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid APIClient credentials')