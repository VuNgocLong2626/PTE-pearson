from fastapi import APIRouter


router = APIRouter(
    prefix="/basic",
    tags=["Basic"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_basic():
    respon = {
        "Name": "Long",
        "Age": 22
    }
    return respon
