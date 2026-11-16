import unittest

from app import app


class TestDevOpsApplication(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(
            data["message"],
            "Welcome to My DevOps CI/CD Project!"
        )

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["status"], "healthy")

    def test_version(self):
        response = self.client.get("/version")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["version"], "1.0")


if __name__ == "__main__":
    unittest.main()
