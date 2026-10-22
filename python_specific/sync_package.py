# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false
# pyright: reportMissingModuleSource=false

# import httpx 
#     response = await httpx.get(
#         "https://api.example.com/exchange-rates",
#         timeout=10,
#     )




import requests

from fastapi import APIRouter

router = APIRouter()


@router.get("/exchange-rates", status_code=200)
async def get_exchange_rates() -> dict:
    response = requests.get(
        "https://api.example.com/exchange-rates",
        timeout=10,
    )
    response.raise_for_status()

    return response.json()