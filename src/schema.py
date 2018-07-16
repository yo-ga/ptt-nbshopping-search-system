import attr


class Post_type:
    SOLD = 0
    PICK = 1
    BUY = 2


@attr.s
class Post_item:
    post_id: int = attr.ib()
    post_url: str = attr.ib()
    post_content: str = attr.ib()
    post_title: str = attr.ib()
    post_type: str = attr.ib()
    post_author: str = attr.ib()
    post_datetime: str = attr.ib()
    post_message: str = attr.ib()


@attr.s
class Product_item(Post_item):
    product_cpu: str = attr.ib()
    product_gpu: str = attr.ib()
    product_price: str = attr.ib()
    product_ram: str = attr.ib()
    product_os: str = attr.ib()
    product_screen: str = attr.ib()

