try:
    from api_movies import app
    import unittest

except Exception as e:
    print("Some Module are Missing {} ".format(e))

class FlaskTest(unittest.TestCase):
    # Check for response 200 in /movies endpoint
    def test_index_movies(self):
        tester = app.test_client(self)
        response = tester.get("/movies")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)
    
    #check if content is application/json in /movies endpoint
    def test_index_content_movies(self):
        tester = app.test_client(self)
        response = tester.get("/movies")
        self.assertEqual(response.content_type, "application/json")

    #check for data returned in /movies endpoint
    def test_index_data_movies(self):
        tester = app.test_client(self)
        response = tester.get("/movies")
        self.assertTrue(b'id' in response.data)
        self.assertTrue(b'original_title' in response.data)
        self.assertTrue(b'budget' in response.data)
        self.assertTrue(b'popularity' in response.data)
        self.assertTrue(b'release_date' in response.data)
        self.assertTrue(b'revenue' in response.data)
        self.assertTrue(b'title' in response.data)
        self.assertTrue(b'vote_average' in response.data)
        self.assertTrue(b'vote_count' in response.data)
        self.assertTrue(b'overview' in response.data)
        self.assertTrue(b'tagline' in response.data)
        self.assertTrue(b'director' in response.data)

    # Check for response 200 in /directors endpoint
    def test_index_directors(self):
        tester = app.test_client(self)
        response = tester.get("/directors")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)
    
    #check if content is application/json in /directors endpoint
    def test_index_content_directors(self):
        tester = app.test_client(self)
        response = tester.get("/directors")
        self.assertEqual(response.content_type, "application/json")

    #check for data returned in /directors endpoint
    def test_index_data_directors(self):
        tester = app.test_client(self)
        response = tester.get("/directors")
        self.assertTrue(b'id' in response.data)
        self.assertTrue(b'name' in response.data)
        self.assertTrue(b'gender' in response.data)
        self.assertTrue(b'uid' in response.data)
        self.assertTrue(b'department' in response.data)
        self.assertTrue(b'movies' in response.data)

if __name__ == "__main__":
    unittest.main()