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
        accesskey = request.GET.get('accesskey')  # visible in URL
        secretkey = request.META.get('secretkey') # HTTP headers (not seen by user)
        
    ### note to self: client actually provides "secretkey" and "accesskey" using those keywords in tests.py

        # Validate that AK and SK were given
        if not accesskey or not secretkey:
            return None

        # Validate that AK and SK are valids
        for key in [accesskey, secretkey]:
            try:
                validate_authkey(key) #function provided above
            except ValidationError:
                raise exceptions.AuthenticationFailed('Invalid APIClient credentials')

        # Validate that APIClient exists for given AK and SK.
        # If it exists and it's active, return a tuple of (api_client, None).
        # Second element in the tuple means that there weren't errors.

        # If APIClient doesn't exist or is inactive, raise an AuthenticationFailed

        ### YOUR CODE HERE
        try:                                 # what happens if you only get one key?
            api_client = APIClient.objects.get(accesskey=accesskey, secretkey=secretkey) # try to get keys from client model
            if api_client.is_active:         # check this field in the model to see if it's True
                return (api_client, None)    # not clear why this is returned this way, brought up in video les
            else:
                raise api_client.DoesNotExist
        except APIClient.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid APIClient credentials')
            
            
# class APIClient(models.Model):
#     name = models.CharField(max_length=128)
#     accesskey = models.CharField(max_length=32)
#     secretkey = models.CharField(max_length=32)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

#     @property
#     def is_staff(self):
#         return True

#     def is_authenticated(self):
#         return True

#     def save(self, *args, **kwargs):
#         self.full_clean()
#         super(APIClient, self).save(*args, **kwargs)