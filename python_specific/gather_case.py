# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


    # user, orders, bonuses = await asyncio.gather(
    #     user_service.get_user(user_id),
    #     order_service.get_user_orders(user_id),
    #     bonus_service.get_user_bonuses(user_id),
    # )



from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}/profile", status_code=200)
async def get_user_profile(user_id: int) -> dict:
    user = await user_service.get_user(user_id)
    orders = await order_service.get_user_orders(user_id)
    bonuses = await bonus_service.get_user_bonuses(user_id)

    return {
        "user": user,
        "orders": orders,
        "bonuses": bonuses,
    }