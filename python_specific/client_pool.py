# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false
# pyright: reportMissingModuleSource=false

# @router.post("/notifications/broadcast", status_code=200)
# async def broadcast_notifications(data: BroadcastRequest) -> dict:
#     async with httpx.AsyncClient(timeout=10) as client:
#         for user_id in data.user_ids:
#             response = await client.post(
#                 "https://api.example.com/notifications",
#                 json={
#                     "user_id": user_id,
#                     "message": data.message,
#                 },
#             )
#             response.raise_for_status()

#     return {"sent": len(data.user_ids)}





@router.post("/notifications/broadcast", status_code=200)
async def broadcast_notifications(data: BroadcastRequest) -> dict:
    for user_id in data.user_ids:
        async with httpx.AsyncClient() as client:
            await client.post(
                "https://api.example.com/notifications",
                json={
                    "user_id": user_id,
                    "message": data.message,
                },
                timeout=10,
            )

    return {"sent": len(data.user_ids)}

 