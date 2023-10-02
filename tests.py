import unittest
from app import app

class TestResumeAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_all_contacts(self):
        response = self.client.get('/get_all_contacts')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(1), data)  # Checking if ID 1 exists in the response

    def test_get_contact_details_valid_id(self):
        response = self.client.get('/get_contact_details/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Rosendo Inzunza')

    def test_get_contact_details_invalid_id(self):
        response = self.client.get('/get_contact_details/999')  # Assuming 999 is an invalid ID
        self.assertEqual(response.status_code, 404)

    def test_get_professional_experience_valid_id(self):
        response = self.client.get('/get_professional_experience/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_professional_experience_invalid_id(self):
        response = self.client.get('/get_professional_experience/999')
        self.assertEqual(response.status_code, 404)

    def test_get_education_valid_id(self):
        response = self.client.get('/get_education/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_education_invalid_id(self):
        response = self.client.get('/get_education/999')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
