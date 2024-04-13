import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from src.python import create_app
        cls.client = create_app().test_client()

    def test_return_hello_world(self):
        response = self.client.get('/api/')

        expected = {'message': 'Hello World'}

        self.assertEqual(response.json, expected)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
