from lxml import html
from requests import get

ROOT_URL = 'https://gippo-market.by'
CATALOG = 'https://gippo-market.by/catalog/'

response = get(CATALOG)
products = []

req_links_categories = '//a[@class="catalog-start__item"]/@href'
dom_catalog = html.fromstring(response.text)
categories = dom_catalog.xpath(req_links_categories)[10:12]

while categories:
    category = categories.pop()
    response = get(f'{ROOT_URL}{category}')

    req_under_category = '//div[@class="link-arrow link-arrow--green"]/a/@href'
    under_category_dom = html.fromstring(response.text)
    under_category = under_category_dom.xpath(req_under_category)

    if under_category:
        print(f'{category} extended {under_category}')
        categories.extend(under_category)
    else:
        print(f'Products found')
        req_products = '//a[contains(@class, "product-card__img-wrap")]/@href'
        products.extend(under_category_dom.xpath(req_products))


for prod in products:
    print(prod)
