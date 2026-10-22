# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false




@router.post("/products/new/import", status_code=200)
async def import_products(
    product_repository: ProductRepository
) -> dict:

    new_products = await get_new_products()

    for product in new_products:
        await product_repository.insert(
            product_id=product.id,
            price=product.price,
        )

    return {"updated": len(new_products)}