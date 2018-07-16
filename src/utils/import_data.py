from requests.auth import HTTPBasicAuth

import json
import os
import pysolr
import re
import attr

from schema import Product_item, Post_type


auth = None


def get_post_id(url):
    return int(re.findall(r'\d+', url)[0])


def detect_post(title):
    if "選購" in title:
        return Post_type.PICK
    elif "賣":
        return Post_type.SOLD
    else:
        return Post_type.BUY


def import_article_to_solr(url):
    pass


def import_articles_to_solr(url_list):
    results = dict()
    results['articles'] = list()
    for url in url_list:
        import_article_to_solr(url)


def import_json_to_solr(json_file):
    data_list = []
    with open(json_file) as f:
        content = f.read()
        data = json.loads(content)
        article_list = data['articles']
        for article in article_list:
            data = {
                "product_price": 0,
                "product_cpu": article['cpu'].strip() if article.get('cpu') else '',
                "product_gpu": article['gpu'].strip() if article.get('gpu') else '',
                "product_ram": article['ram'].strip() if article.get('ram') else '',
                "product_os": article['os'].strip() if article.get('os') else '',
                "product_screen": article['screen'].strip() if article.get('screen') else '',
                "post_id": get_post_id(article['url']),
                "post_url": article['url'],
                "post_content": article['content'].strip(),
                "post_title": article['article_title'].strip(),
                "post_type": detect_post(article['article_title']),
                "post_author": article['author'].strip(),
                "post_datetime": article['date'].strip(),
                "post_message": ' '.join(article['messages'])
            }

            if article['price']:
                if isinstance(article['price'], int):
                    data['product_price'] = article['price']
                else:
                    data['product_price'] = int(re.findall('\d+', article['price'])[0])
            else:
                data['product_price'] = None

            product = Product_item(**data)

            item = attr.asdict(product)
            item['id'] = product.post_id
            data_list.append(item)

    solr = pysolr.Solr('http://{localhost}:8983/solr/ptt'.format(localhost=os.getenv("SOLR_HOST", "localhost")), auth=auth)
    solr.add(data_list)

