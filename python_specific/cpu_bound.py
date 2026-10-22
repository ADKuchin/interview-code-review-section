# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false
# pyright: reportMissingModuleSource=false


# @router.get("/statistics/yearly", status_code=200)
# async def get_yearly_statistics(year: int) -> dict:
#     statistics = await run_in_threadpool(
#         statistics_service.calculate_year_statistics,
#         year,
#     )

#     return {"statistics": statistics}


from fastapi import APIRouter

router = APIRouter()


@router.get("/statistics/yearly", status_code=200)
async def get_yearly_statistics(year: int) -> dict:
    statistics = statistics_service.calculate_year_statistics(year)

    return {"statistics": statistics}