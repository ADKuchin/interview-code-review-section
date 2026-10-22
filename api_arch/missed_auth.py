# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


from fastapi import APIRouter

router = APIRouter()


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int) -> None:
    await user_service.delete_user(user_id)




@router.patch("/users/{user_id}/avatar", status_code=200)
async def update_avatar(
    user_id: int,
    data: UpdateAvatarRequest,
) -> dict:
    await user_service.update_avatar(
        user_id=user_id,
        avatar_url=data.avatar_url,
    )

    return {"message": "Avatar updated"}