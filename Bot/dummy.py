from datetime import datetime
from models import Category, SubCategory, Products, SKU, SalesUnit, Date

created_date = Date(year=2025, month=12, day=18, hour=11)
updated_date = Date(year=2026, month=1, day=5, hour=16)

database_sales_unit = SalesUnit(
    unit_name="Silverleaf Arcane Bazaar",
    unit_code="SLV-LF-01",
    unit_location="Eldoria Central Spire",
    street="Moonveil Avenue",
    city="Eldoria",
    district="High Canopy",
    state="Kingdom of Aelwyn",
    pincode="ELD-90231",
    latitude=45.7721,
    longitude=-12.3349,
    contact_number="+999-ELF-7788",
    email="trade@silverleaf.guild",
    status="ENCHANTED_ACTIVE",
    created_at=created_date,
    updated_date=updated_date,
    gst_number="AE-LF-ARC-88991",
    delvery_radius=120
)


database_category = Category(
    category_id="CAT-ARC-001",
    category_name="Arcane Provisions",
    category_code="ARC-PROV",
    created_at=created_date,
    updated_date=updated_date,
    icon_url="https://fantasy.assets/icons/arcane.png",
    standard_image_url="https://fantasy.assets/images/arcane_standard.png",
    banner_image_url="https://fantasy.assets/banners/arcane_banner.png",
    sales_unit=[database_sales_unit],
    long_distance_availability=True
)
database_subcategory = SubCategory(
    sub_category_id="SUB-ARC-ELX",
    sub_category_name="Mystic Elixirs",
    sub_category_code="ELIX",
    category=database_category,
    standard_image_url="https://fantasy.assets/images/elixirs.png",
    created_at=created_date,
    updated_date=updated_date,
    sales_unit=[database_sales_unit],
    long_distance_availability=True
)

database_product = Products(
    product_type="ALCHEMY",
    item_name="Elixir of Dragon’s Vitality",
    item_code="ELX-DRG-VIT",
    item_category=database_category,
    item_subcategory=database_subcategory,
    item_description=(
        "A potent crimson elixir brewed from dragon scale dust "
        "and firebloom petals. Restores stamina and resilience."
    ),
    veg_ornon_veg_status="NON_VEG",
    i_gst=0.0,
    s_gst=6.5,
    c_gst=6.5,
    cess=1.2,
    created_date=created_date,
    updated_date=updated_date,
    sales_unit=[database_sales_unit],
    long_distance_availability=True
)


fantasy_sku = SKU(
    product=[database_product],
    sku_name="Dragon Vitality Elixir – 500ml Flask",
    sku_code="SKU-DRG-VIT-500",
    sku_quantity=500,
    sku_unit="ML",
    sku_mrp=2499.99,
    sku_expiry_duration=365,
    sku_bulk_quantity=20,
    sku_status="ARCANE_APPROVED",
    created_at=created_date,
    sales_unit=[database_sales_unit],
    long_distance_availability=True,
    same_day_delivery=False,
    customization_available=True
)
