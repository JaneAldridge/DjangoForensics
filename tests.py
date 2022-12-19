from django.test import TestCase

# Test that the login URL works and that the user id and password are returned successfully
# self.client.get is a Django test client  
class URLTesting(TestCase):
    def url_login_test(self):
        response = self.client.get('/login')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
# test the user id and password from the login page 
        assert 'name="username"' in html
        assert 'name="password"' in html
        assert 'name="submit"' in html

# test if a valid user can login using a test user id and test password 
    def check_user_login_valid(self):
        response = self.client.post('/login', data={
            'username': 'Officer',
            'password': 'essex123',
        }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/login'

# test to check if a invalid user cannot login
def check_user_login_invalid(self):
        response = self.client.post('/login', data={
            'username': 'janealdridge',
            'password': 'essex123',
        })
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Invalid User Id' in html

# test to check if a invalid password cannot login
def check_user_login_invalid(self):
        response = self.client.post('/login', data={
            'username': 'Officer',
            'password': 'surrey123',
        })
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Invalid password' in html

        





