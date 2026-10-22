# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false







# CREATE INDEX idx_user_products_user_id
# ON user_products (user_id);







"""
CREATE TABLE user_products (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id),
    product_id BIGINT NOT NULL REFERENCES products(id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
"""


@router.get("/users/{user_id}/products", status_code=200)
async def get_user_products(user_id: int) -> dict:
    query = """
        SELECT id, product_id, quantity
        FROM user_products
        WHERE user_id = :user_id
    """

    products = await db.fetch_all(
        query=query,
        values={"user_id": user_id},
    )

    return {"products": products}