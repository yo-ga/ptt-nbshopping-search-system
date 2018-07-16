from requests.auth import HTTPBasicAuth

import os
import pysolr

from schema import Post_type


solr_host = os.getenv("SOLR_HOST", "localhost")
auth = None
solr = pysolr.Solr('http://{}:8983/solr/ptt'.format(solr_host), auth=auth)


def product_search(query=None, price=None, screen=None, ram=None):
    q = ''
    if query:
        query_str = '+'.join(query.split(' '))
        q += 'post_content:' + query_str + ' OR post_content:' + query_str
    else:
        q += '*:*'
    if price and price != '0':
        if price == '10000':
            q += ' AND product_price:[* TO 10000]'
        elif price == '20000':
            q += ' AND product_price:[10000 TO 20000]'
        elif price == '30000':
            q += ' AND product_price:[20000 TO 30000]'
        elif price == '40000':
            q += ' AND product_price:[30000 TO 40000]'
        elif price == '50000':
            q += ' AND product_price:[40000 TO 50000]'
        elif price == '60000':
            q += ' AND product_price:[50000 TO *]'
    if screen and screen != '0':
        if screen == '14':
            q += ' AND product_screen:[* TO 14]'
        elif screen == '15':
            q += ' AND product_screen:15'
        elif screen == '16':
            q += ' AND product_screen:16'
        elif screen == '17':
            q += ' AND product_screen:[17 TO *]'
    if ram and ram != 0:
        if ram == '4':
            q += ' AND product_ram:4'
        elif ram == '8':
            q += ' AND product_ram:8'
        elif ram == '16':
            q += ' AND product_ram:16'
    result = solr.search(q=q, **{
        'fq': 'post_type:{}'.format(Post_type.SOLD),
        'rows': '900',
        'sort': "score desc, id desc",
    })
    return result.docs


def pick_search(query=None, price=None, screen=None, ram=None):
    q = ''
    if query:
        query_str = '+'.join(query.split(' '))
        q += 'post_content:' + query_str + ' OR post_content:' + query_str
    else:
        q += '*:*'
    if price and price != '0':
        if price == '10000':
            q += 'OR post_content:10K'
        elif price == '20000':
            q += 'OR post_content:20K'
        elif price == '30000':
            q += 'OR post_content:30K'
        elif price == '40000':
            q += 'OR post_content:40K'
        elif price == '50000':
            q += 'OR post_content:50K'
        elif price == '60000':
            q += 'OR post_content:60K'
    result = solr.search(q=q, **{
        'rows': '900',
        'fq': 'post_type:{}'.format(Post_type.PICK),
        'sort': "score desc, id desc",
    })
    return result.docs
