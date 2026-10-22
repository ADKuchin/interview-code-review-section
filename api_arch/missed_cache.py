# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false


# @router.get("/categories", status_code=200)
# async def get_categories() -> dict:
#     cached = await redis.get("categories")

#     if cached is not None:
#         return json.loads(cached)

#     categories = await category_repository.get_all()
#     response = {"categories": categories}

#     await redis.set(
#         "categories",
#         json.dumps(response),
#         ex=300,
#     )

#     return response



from fastapi import APIRouter

router = APIRouter()


@router.get("/categories", status_code=200)
async def get_categories() -> dict:
    categories = await category_repository.get_all()

    return {"categories": categories}