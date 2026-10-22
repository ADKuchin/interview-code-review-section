# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false





class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int


@router.post("/cart/items", status_code=201)
async def add_to_cart(data: AddToCartRequest) -> dict:
    await cart_service.add_item(
        product_id=data.product_id,
        quantity=data.quantity,
    )

    return {"message": "Product added to cart"}