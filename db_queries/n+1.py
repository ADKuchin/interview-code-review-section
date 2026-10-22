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
#         SELECT
#             u.id AS user_id,
#             u.username,
#             o.id AS order_id,
#             o.total
#         FROM users u
#         LEFT JOIN orders o ON u.id = o.user_id
#     """

#     rows = await db.fetch_all(query)

#     users = {}

#     for row in rows:
#         user_id = row["user_id"]

#         if user_id not in users:
#             users[user_id] = {
#                 "username": row["username"],
#                 "orders": [],
#             }

#         if row["order_id"] is not None:
#             users[user_id]["orders"].append({
#                 "id": row["order_id"],
#                 "total": row["total"],
#             })

#     return {"users": list(users.values())}











# @router.get("/users", status_code=200)
# async def get_users() -> dict:
#     users = await db.fetch_all("SELECT id, username FROM users")

#     result = []

#     for user in users:
#         orders = await db.fetch_all(
#             "SELECT id, total FROM orders WHERE user_id = :user_id",
#             values={"user_id": user["id"]},
#         )

#         result.append({
#             "username": user["username"],
#             "orders": orders,
#         })

#     return {"users": result}











@router.get("/users", status_code=200)
async def get_users(
    session: AsyncSession = Depends(get_session),
) -> dict:
    result = await session.execute(select(User))
    users = result.scalars().all()

    return {
        "users": [
            {
                "username": user.username,
                "orders": user.orders,
            }
            for user in users
        ]
    }






# @api_view(["GET"])
# def get_users(request):
#     users = User.objects.prefetch_related("orders")

#     return Response({
#         "users": [
#             {
#                 "username": user.username,
#                 "orders": [
#                     {
#                         "id": order.id,
#                         "total": order.total,
#                     }
#                     for order in user.orders.all()
#                 ],
#             }
#             for user in users
#         ]
#     })







# @api_view(["GET"])
# def get_users(request):
#     users = User.objects.all()

#     return Response({
#         "users": [
#             {
#                 "username": user.username,
#                 "orders": list(
#                     user.orders.values("id", "total")
#                 ),
#             }
#             for user in users
#         ]
#     })