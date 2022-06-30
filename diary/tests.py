from django.test import TestCase, Client

# Create your tests here.
import json

class PostApiTest(TestCase):
    fixtures = ['initial.json']

    def test_list(self):
        response = Client().get(
            '/api/posts/',
        )
        print(json.dumps(response.json(), indent=4))

    def test_retrieve(self):
        response = Client().get(
            '/api/posts/1/',
        )
        print(json.dumps(response.json(), indent=4))

    def test_create(self):
        response = Client().post(
            '/api/posts/',
            data={
                'title': 'hoge',
                'body': 'body desu',
                'user': 1,
            }
        )
        print(response.status_code)
        print(json.dumps(response.json(), indent=4))

