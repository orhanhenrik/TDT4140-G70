import base64
import json

import requests
from django.conf import settings


class Elasticsearch:
    def __init__(self, ES_URL=None):
        if ES_URL is None:
            ES_URL = settings.ES_URL
        self.ES_URL = ES_URL
        self.default_index = 'my_index'
        self.default_type = 'my_type'

    def add_to_index(self, id, filename, data, index=None, type=None):
        if index is None:
            index = self.default_index
        if type is None:
            type = self.default_type

        b64_string = base64.b64encode(data)
        r = requests.post(
            '{}{}/{}/{}?pipeline=attachment'.format(self.ES_URL, index, type, id),
            data=json.dumps({
                "filename": filename,
                "data": b64_string.decode('utf-8')
            })
        )
        return r
        #print(r)
        #print(r.text)
        #print(r.status_code)

    def search(self, query, index=None, type=None):
        if index is None:
            index = self.default_index
        if type is None:
            type = self.default_type

        r = requests.post(
            '{}{}/{}/_search'.format(self.ES_URL, index, type),
            data=json.dumps({
                '_source': {
                    'includes': ['filename']
                },
                'query': {
                    'multi_match': {
                        'query': query,
                        'fuzziness': 'AUTO',
                        'fields': ['attachment.content', '_source.filename']
                    }
                },
                "highlight": {
                    "pre_tags": ["<b>"],
                    "post_tags": ["</b>"],
                    "fields": {
                        "attachment.content": {
                            "fragment_size": 150,
                            "number_of_fragments": 3
                        }
                    }
                }
            })
        )
        return json.loads(r.text)

elasticsearch = Elasticsearch()