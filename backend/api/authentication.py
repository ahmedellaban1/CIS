from rest_framework.authentication import TokenAuthentication as BaseAuthentication
from rest_framework.authtoken.models import Token
class TokenAuthentication(BaseAuthentication):
    keyword = "Bearer"