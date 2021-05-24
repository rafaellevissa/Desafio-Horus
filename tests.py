import unittest
import json
from server import app

class Home(unittest.TestCase):
  def test_get(self):
    application = app.test_client()
    response = application.get('/')
    self.assertEqual(200, response.status_code)

class TestContacts(unittest.TestCase):
  def test_get(self):
    application = app.test_client()
    response = application.get('/contacts')
    self.assertEqual(200, response.status_code)
    self.assertIn('application/json', response.content_type)

  def test_set(self):
    application = app.test_client()
    
    data = { 'name': 'Teste2', 'phone': '7199828387' }
    headers={'Content-Type': 'application/json'}

    response = application.post('/contact/insert', data=json.dumps(data), headers=headers)
    
    self.assertEqual(200, response.status_code)
    self.assertIn('application/json', response.content_type)

if __name__ == '__main__':
  unittest.main()