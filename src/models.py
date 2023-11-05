from pydantic import BaseModel


class ItemPayload(BaseModel):
    item_id: int | None
    item_name: str
    quantity: int
