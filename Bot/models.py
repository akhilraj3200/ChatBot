from __future__ import annotations
from pydantic import BaseModel

class Date(BaseModel):
    # Somehow LLM is bad at specifying `datetime.datetime`, so
    # we define a custom class to represent the date.
    year: int
    month: int
    day: int
    hour: int

class SalesUnit(BaseModel):
    unit_name: str
    unit_code: str
    unit_location: str
    street: str
    city: str
    district: str
    state: str
    pincode: str
    latitude: float
    longitude: float
    contact_number: str
    email: str
    status: str
    created_at: Date
    updated_date: Date
    gst_number: str
    delvery_radius: int



class Category(BaseModel):
    category_id: str
    category_name: str
    category_code:str
    created_at: Date
    updated_date: Date
    icon_url: str
    standard_image_url: str
    banner_image_url: str
    sales_unit:list[SalesUnit]
    long_distance_availability: bool

class SubCategory(BaseModel):
    sub_category_id: str
    sub_category_name: str
    sub_category_code: str
    category: Category
    standard_image_url: str
    created_at: Date
    updated_date: Date
    sales_unit: list[SalesUnit]
    long_distance_availability: bool


class Products(BaseModel):
    product_type: str
    item_name: str
    item_code: str
    item_category: Category
    item_subcategory: SubCategory
    item_description: str
    veg_ornon_veg_status: str
    i_gst: float
    s_gst: float
    c_gst: float
    cess: float
    created_date: Date
    updated_date: Date
    sales_unit: list[SalesUnit]
    long_distance_availability: bool

class SKU(BaseModel):
    product: list[Products]
    sku_name:str
    sku_code:str
    sku_quantity: int
    sku_unit: str
    sku_mrp: float
    sku_expiry_duration: int
    sku_bulk_quantity: int
    sku_status: str
    created_at: Date
    sales_unit:list[SalesUnit]
    long_distance_availability: bool
    same_day_delivery: bool
    customization_available: bool

