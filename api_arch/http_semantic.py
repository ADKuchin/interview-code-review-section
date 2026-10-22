# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false




@router.get("/orders/{order_id}/cancel", status_code=200)
async def cancel_order(order_id: int) -> dict:
    await order_service.cancel_order(order_id)

    return {"message": "Order cancelled"}





@router.get("/users/{user_id}/wallet", status_code=200)
async def get_wallet(user_id: int) -> dict:
    user = await user_service.get_user(user_id)

    wallet = await wallet_service.get_wallet(user_id)

    if wallet is None:
        wallet = await wallet_service.create_wallet(user_id)

    return {
        "user": user,
        "wallet": wallet,
    }