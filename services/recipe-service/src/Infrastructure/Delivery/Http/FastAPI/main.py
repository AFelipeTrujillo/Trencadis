from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi import status
from Domain.Exception.DomainException import DomainException
from Infrastructure.Delivery.Http.Security.KeycloakGuard import KeycloakGuard

app = FastAPI(title="Trencadís Recipe Service", version="1.0.0")
auth_guard = KeycloakGuard()

@app.get("/recipes")
def get_recepies(user: dict = Depends(auth_guard)):
    return {
        "message": "Authenticated access to recipes",
        "user_id": user.get("sub")
    }

@app.exception_handler(DomainException)
def domain_exception_handler(request, exc: DomainException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Domain Error",
            "type": exc.__class__.__name__,
            "message": str(exc)
        },
    )