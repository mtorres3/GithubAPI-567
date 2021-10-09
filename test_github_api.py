import unittest
from unittest import mock
from github_api import repo_amount

class TestGithubApi(unittest.TestCase):
    mock_request = mock.Mock()

    @mock.patch('github_api.requests.get')
    def testInvalidUser(self, mock_request):
        self.assertEqual(repo_amount(4), "Invalid user data")
        self.assertEqual(repo_amount(8.52), "Invalid user data")

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
