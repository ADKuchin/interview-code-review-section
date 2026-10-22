# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


# @router.get("/products")
# async def get_products(
#     limit: int = Query(default=20, ge=1, le=100),
#     offset: int = Query(default=0, ge=0),
# ) -> dict:
#     query = """
#         SELECT id, name, price
#         FROM products
#         WHERE is_active = TRUE
#         ORDER BY created_at DESC, id DESC
#         LIMIT :limit OFFSET :offset
#     """

#     products = await db.fetch_all(
#         query=query,
#         values={"limit": limit, "offset": offset},
#     )

#     return {"products": products, "status_code": 200}

















@router.get("/products", status_code=200)
async def get_products() -> dict:
    query = """
        SELECT id, name, price
        FROM products
        WHERE is_active = TRUE
        ORDER BY created_at DESC
    """

    products = await db.fetch_all(query)

    return {"products": products}