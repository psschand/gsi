
import unittest
import os
import json

from .app import app



class UsersTest(unittest.TestCase):
  """
  Users Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = app
    self.client = self.app.test_client
    self.user = {
         "username": "user1",
         "password":"password1"
    }

  
  def test_user_creation(self):
    """ test user creation with valid credentials """
    res = self.client().post('/login', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertTrue(json_data.get('jwt_token'))
    self.assertEqual(res.status_code, 200)

#   def test_user_creation_with_existing_password(self):


  def test_user_login_creation_with_no_password(self):
    """ test user login creation with no password"""
    user1 = {
      "username": "user1"
     
    }
    res = self.client().post('/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    # self.assertTrue(json_data)
    self.assertEqual(res.status_code, 401)
    self.assertTrue(json_data.get('message'))
    self.assertEqual(json_data.get('message'), "invalid message")


  def test_user_login_with_invalid_password(self):
    """ User Login Tests with invalid credentials """
    user2 = {
      "username": "user1",
       "password":"wrong pass word"
    }
    res = self.client().post('/login', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 200)
    res = self.client().post('/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user2))
    json_data = json.loads(res.data)
    self.assertFalse(json_data.get('jwt_token'))
    self.assertEqual(json_data.get('message'), 'login required')
    self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
  unittest.main() 
