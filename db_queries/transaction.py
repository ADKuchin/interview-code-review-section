# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false






@router.post("/products/purchase", status_code=201)
async def purchase_product(data: PurchaseProductRequest) -> dict[str, str | int]:
    product = await get_product(data.product_id)

    await withdraw_money(data.user_id, product.price)

    await add_product_to_inventory(
        data.user_id,
        data.product_id,
    )

    return {"status": "success"}





@router.post("/orders", status_code=201)
async def create_order(
    data: CreateOrderRequest,
) -> dict[str, str | int]:
    order = await save_order(
        user_id=data.user_id,
        product_id=data.product_id,
        quantity=data.quantity,
    )

    await kafka_producer.send_and_wait(
        "orders.created",
        {
            "order_id": order.id,
            "user_id": data.user_id,
        },
    )

    return {"status": "success"}