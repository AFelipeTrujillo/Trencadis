from fastapi import FastAPI, Depends
from Infrastructure.Delivery.Http.Security.KeycloakGuard import KeycloakGuard

app = FastAPI(title="Trencadís Recipe Service", version="1.0.0")
auth_guard = KeycloakGuard()

@app.get("/recipes")
def get_recepies(user: dict = Depends(auth_guard)):
    return {
        "message": "Authenticated access to recipes",
        "user_id": user.get("sub")
    }
    