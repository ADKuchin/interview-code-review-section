# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


from fastapi import APIRouter, HTTPException

router = APIRouter()



@router.post("/users", status_code=200)
async def create_user(data: CreateUserRequest) -> dict:
    user = await user_service.create_user(data)

    return {"user_id": user.id}


@router.delete("/users/{user_id}", status_code=201)
async def delete_user(user_id: int) -> dict:
    deleted = await user_service.delete_user(user_id)

    if not deleted:
        raise HTTPException(status_code=500, detail="User not found")

    return {"message": "User deleted"}