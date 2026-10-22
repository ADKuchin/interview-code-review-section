# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false



# @router.get("/users", status_code=200)
# async def get_users() -> dict:
#     query = """
#         SELECT id, username, avatar_url
#         FROM users
#         WHERE is_active = TRUE
#         LIMIT 100
#     """

#     users = await db.fetch_all(query)

#     return {"users": users}








@router.get("/users", status_code=200)
async def get_users() -> dict:
    query = """
        SELECT *
        FROM users
        WHERE is_active = TRUE
        LIMIT 100
    """

    users = await db.fetch_all(query)

    return {
        "users": [
            {
                "id": user["id"],
                "username": user["username"],
                "avatar_url": user["avatar_url"],
            }
            for user in users
        ]
    }