from locust import HttpUser, task

class TestUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    @task
    def get_user(self):
        self.client.get("/users/1")