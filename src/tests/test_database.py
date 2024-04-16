import unittest

from database.db import change_to_memory_database


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        change_to_memory_database()
        from src.python import create_app
        cls.client = create_app().test_client()

    def test_save_todo_to_db(self):
        response = self.client.get('/api/save')
        print(response.json)


if __name__ == '__main__':
    unittest.main()
