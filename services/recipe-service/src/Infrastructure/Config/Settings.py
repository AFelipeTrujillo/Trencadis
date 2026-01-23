from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):

    PROJECT_NAME: str = "Trencadís Recipe Service"
    DEBUG: bool = False

    KEYCLOAK_BASE_URL : str = Field(default="http://keycloak:8080/realms/", env="KEYCLOAK_BASE_URL")
    KEYCLOAK_REALM : str = Field(default="trencadis-home", env="KEYCLOAK_REALM")

    @property
    def keycloak_realm_url(self) -> str:
        return f"{self.KEYCLOAK_BASE_URL}/realms/{self.KEYCLOAK_REALM}"

    @property
    def keycloak_jwks_url(self) -> str:
        return f"{self.keycloak_realm_url}/protocol/openid-connect/certs"

    @property
    def keycloak_auth_url(self) -> str:
        return f"{self.keycloak_realm_url}/protocol/openid-connect/auth"

    @property
    def keycloak_token_url(self) -> str:
        return f"{self.keycloak_realm_url}/protocol/openid-connect/token"
    
    DATABASE_URL : str = Field(default="postgresql://user:pass@localhost:5432/recipes", env="DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Create a single settings instance to be used across the application
settings = Settings()
