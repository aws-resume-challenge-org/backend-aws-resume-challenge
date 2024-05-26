import unittest
import requests
from lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):

    def test_lambda_handler(self):
        # Define the API endpoint that provides the visitor count
        api_endpoint = 'https://7vgsgyibz8.execute-api.us-west-2.amazonaws.com/getVisitorCount'
        
        # Call lambda_handler
        result = lambda_handler({}, None)

        # Fetch the real visitor count from the API
        try:
            response = requests.get(api_endpoint)
            response.raise_for_status()
            real_visitor_count = int(response.text) - 1  # Convert the response directly to an integer
        except (requests.RequestException, ValueError) as e:
            # If unable to fetch the count from API or conversion fails, use default value
            real_visitor_count = 0
        
        # Verify result
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('body', result)
        self.assertEqual(int(result['body']), real_visitor_count)  # Convert to integer before comparison

if __name__ == '__main__':
    unittest.main()
