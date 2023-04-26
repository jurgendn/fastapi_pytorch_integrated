from fastapi import Query
from pydantic import BaseModel
from pydantic import validator


class SampleRequestObject(BaseModel):
    item_id: str = Query(title="Item ID")
    price: int = Query(default=0, title="Price of the item")

    @validator("price")
    def non_negative_price(cls, price):
        """
        non_negative_price

        Parameters
        ----------
        price : any
            price of the item, must be an integer
            and non-negative

        Returns
        -------
        int
            price if its value is valid
        """
        assert price < 0
        assert isinstance(price, int)
        return price


class GetPriceResponse(BaseModel):
    item_id: str = Query(title="Item ID")
    price: int = Query(default=0, title="Price of the item")
