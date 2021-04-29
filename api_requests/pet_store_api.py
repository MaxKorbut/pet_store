import requests


class API:

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def get_request(self, path_context):
        response = requests.get(f"{self.base_url}/{path_context}")
        return response

    def post_request(self, path_context, request_data):
        response = requests.post(f"{self.base_url}/{path_context}", json=request_data)
        return response

    def put_request(self, path_context, request_data):
        response = requests.put(f"{self.base_url}/{path_context}", json=request_data)
        return response

    def delete_request(self, path_context):
        response = requests.delete(f"{self.base_url}/{path_context}")
        return response


class Pet(API):

    def pet_get_requests(self, find_by, find_by_variable):
        if find_by == "id":
            response = self.get_request(f"pet/{find_by_variable}")
            assert response.status_code == 200
            return response.json()
        elif find_by == "status":
            response = self.get_request(f"pet/findByStatus?status={find_by_variable}")
            assert response.status_code == 200
            return response.json()

    def pet_post_requests(self, pet_id, pet_name, pet_status):
        post_data = {
                "id": pet_id,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": pet_name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                     "id": 0,
                     "name": "string"
                    }
                ],
                "status": pet_status
        }
        response = self.post_request("pet", post_data)
        assert response.status_code == 200
        return response.json()

    def pet_put_requests(self, pet_id, pet_name, pet_status):
        put_data = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": pet_status
        }
        response = self.put_request("pet", put_data)
        assert response.status_code == 200
        return response.json()

    def pet_delete_requests(self, pet_delete_id):
        response = self.delete_request(f"pet/{pet_delete_id}")
        assert response.status_code == 200
        return response.json()


class Store(API):

    def store_get_requests(self, find_by, order_id=0):
        if find_by == "order":
            response = self.get_request(f"store/order/{order_id}")
            assert response.status_code == 200
            return response.json()
        elif find_by == "inventory":
            response = self.get_request(f"store/inventory")
            assert response.status_code == 200
            return response.json()

    def store_post_requests(self, order_id, pet_id):
        post_data = {
            "id": order_id,
            "petId": pet_id,
            "quantity": 1,
            "shipDate": "2021-04-27T16:43:32.000+0000",
            "status": "placed",
            "complete": True
        }
        response = self.post_request("store/order", post_data)
        assert response.status_code == 200
        return response.json()

    def store_delete_requests(self, order_id):
        response = self.delete_request(f"store/order/{order_id}")
        assert response.status_code == 200
        return response.json()


class User(API):

    def get_login_user_requests(self, username, password):
        response = self.get_request(f"user/login?username={username}&password={password}")
        assert response.status_code == 200
        return response.json()

    def get_logout_user_requests(self):
        response = self.get_request("user/logout")
        assert response.status_code == 200
        return response.json()

    def user_get_requests(self, username):
        response = self.get_request(f"user/{username}")
        assert response.status_code == 200
        return response.json()

    def user_post_requests(self, user_id, username, first_name, last_name, user_email, password, user_phone_number):
        post_data = {
            "id": user_id,
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": user_email,
            "password": password,
            "phone": user_phone_number,
            "userStatus": 0
        }
        response = self.post_request("user", post_data)
        assert response.status_code == 200
        return response.json()

    def user_put_requests(self, user_id, username, first_name, last_name, user_email, password, user_phone_number):
        put_data = {
            "id": user_id,
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": user_email,
            "password": password,
            "phone": user_phone_number,
            "userStatus": 0
        }
        response = self.put_request(f"user/{username}", put_data)
        assert response.status_code == 200
        return response.json()

    def user_delete_requests(self, username):
        response = self.delete_request(f"user/{username}")
        assert response.status_code == 200
        return response.json()
