import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]
    current_page = 1

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            image_div = product.css(".product-item_img-box .image-filler:first-child")
            image_name = f"https://www.oma.by{image_div.attrib.get('data-img-src')}"
            data = {
                "external_id": int(product.attrib.get("data-ga-product-id")),
                "name": product.attrib.get("data-ga-product-name").strip(),
                "price": product.attrib.get("data-ga-product-price").strip(),
                "category": product.attrib.get("data-ga-category-last").strip(),
                "image_name": image_name,
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
            }
            yield data

        next_page = response.css(
            ".page-nav_box .btn__page-nav:last-child::attr(href)"
        ).get()
        if next_page is not None:
            self.current_page += 1
            if self.current_page == 2:
                return
            yield response.follow(next_page, callback=self.parse)
