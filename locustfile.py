from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    # Указываем базовый хост (например, для локального сервера)
    host = "http://localhost:8000"

    # Пауза между запросами (от 1 до 2 секунд)
    wait_time = between(1, 2)

    @task
    def login(self):
        response = self.client.post("/login/", {
            "username": "testuser",
            "password": "password123"
        })
        print("Login status:", response.status_code)

    @task
    def some_page(self):
        self.client.get("/")

    @task
    def go_to_schedules(self):
        # Переход на страницу календаря, например '/schedules/'
        response = self.client.get("/schedules/")
        print("Schedules page status:", response.status_code)
