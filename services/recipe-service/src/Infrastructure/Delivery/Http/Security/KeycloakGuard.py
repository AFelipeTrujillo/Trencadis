import httpx
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="http://localhost:8080/realms/trencadis/protocol/openid-connect/token",
)

class KeycloakGuard:

    def __init__(self):
        self.realm_url = "http://localhost:8080/realms/trencadis"
        self.public_key = self.get_public_key()

    def get_public_key(self) -> str:
        # In a real implementation, fetch the public key from Keycloak's JWKS endpoint
        response = httpx.get(f"{self.realm_url}")
        return f"-----BEGIN PUBLIC KEY-----\n{response.json()['public_key']}\n-----END PUBLIC KEY-----"
    
    async def __call__(self, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, self.public_key, algorithms=["RS256"], audience="account")
            # You can add more checks here, like verifying roles or permissions
            # Return authenticated user info if needed (sub, roles, etc.)
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
