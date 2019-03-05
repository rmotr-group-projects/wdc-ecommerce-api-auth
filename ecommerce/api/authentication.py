from django.core.exceptions import ValidationError
from rest_framework import exceptions, permissions, authentication
from api.models import APIClient


def validate_authkey(value):
    """Raises a ValidationError if value has not length 32"""
    if len(value) != 32:
        raise ValidationError(
            'Your value must be a string of 32 letters and numbers')


class APIClientAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):    # overriding this method from default
        # Get the accesskey from the query parameters, and the secretkey from
        # the request headers.
        accesskey = request.query_params.get('accesskey')   # from DRF... Is also request.GET, but is more specific
        secretkey = request.META.get('secretkey')   # HTTP headers

        # Validate that AK and SK were given
        if not accesskey or not secretkey:
            return None

        # validate that AK and SK are valids
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



        # validate that APIClient exists for given AK and SK
        try:
            api_client = APIClient.objects.get(accesskey=accesskey, secretkey=secretkey)
            if api_client.is_active:
                return (api_client, None)
            else:
                raise api_client.DoesNotExist
        except APIClient.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid APIClient credentials')
