from pydantic import BaseModel, root_validator


class Price_name(BaseModel):
    basic: float
    total: float 

    @root_validator(pre=True)
    def conver_sale(cls, values: dict):
        basic_price = values.get("basic")
        total_price = values.get("total")
        if basic_price is not None:
            values["basic"] = basic_price / 100
        if total_price is not None:
            values["total"] = total_price / 100
        return values
    
class Sizes_name(BaseModel):
    price: Price_name  # Изменено на объект, а не список


class Item(BaseModel):
    id: int
    brand: str
    name: str
    sizes: list[Sizes_name]
    totalQuantity: int

    
class Products_name(BaseModel):
    products: list[Item]
