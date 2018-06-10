import attr

@attr.s
class Product_item:
    pid: int = attr.ib()
    product_name: str = attr.ib()
    product_link: str = attr.ib()
    product_price: int = attr.ib()
    product_content: str = attr.ib()


@attr.s
class Post_item:
    pass
