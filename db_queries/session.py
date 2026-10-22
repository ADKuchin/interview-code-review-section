# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


# @router.get("/users/{user_id}", status_code=200)
# async def get_user(user_id: int) -> dict:
#     async with async_session_maker() as session:
#         result = await session.execute(
#             select(User).where(User.id == user_id)
#         )

#         user = result.scalar_one_or_none()

#         return {"user": user}






# async def get_session():
#     async with async_session_maker() as session:
#         yield session


# @router.get("/users/{user_id}", status_code=200)
# async def get_user(
#     user_id: int,
#     session: AsyncSession = Depends(get_session),
# ) -> dict:
#     result = await session.execute(
#         select(User).where(User.id == user_id)
#     )

#     user = result.scalar_one_or_none()

#     return {"user": user}













@router.get("/users/{user_id}", status_code=200)
async def get_user(user_id: int) -> dict:
    session = async_session_maker()

    result = await session.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    return {"user": user}