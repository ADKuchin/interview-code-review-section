# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false

# GET /auth/login?username=alex&password=secret123



from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/auth/login", status_code=200)
async def login(
    username: str = Query(),
    password: str = Query(),
) -> dict:
    user = await auth_service.authenticate(
        username=username,
        password=password,
    )

    token = await auth_service.create_access_token(user.id)

    return {"access_token": token}