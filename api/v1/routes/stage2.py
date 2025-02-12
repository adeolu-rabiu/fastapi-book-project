from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/stage2-endpoint", status_code=404)  # Set explicit status code
async def stage2_not_implemented():
    raise HTTPException(status_code=404, detail="Not Implemented")
