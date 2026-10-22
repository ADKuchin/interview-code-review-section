# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false



    #   user = await db.fetch_one(
    #       query=query,
    #       values={"username": username},
    #   )


# @router.get("/users/{username}")
# async def get_user(username: str) -> dict:
#     query = """
#         SELECT *
#         FROM users
#         WHERE username = $1
#     """

#     user = await conn.fetchrow(query, username)

#     return {"user": dict(user) if user else None}


















@router.get("/users/{username}", status_code=200)
async def get_user(username: str) -> dict:
    query = f"SELECT * FROM users WHERE username = {username}"

    user = await db.fetch_one(query)

    return {"user": user}