from fastapi import APIRouter

from interfaces.item import GetPriceResponse, SampleRequestObject

router = APIRouter(prefix="/some-router")


@router.get(path="/item-price", response_model=GetPriceResponse)
async def get_price(item: SampleRequestObject) -> GetPriceResponse:
    return GetPriceResponse(item_id=item.item_id, price=item.price)
