from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):

    @task(1)
    def create_post(self):
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        self.client.post("/arama?q=iphone", data=json.dumps({
            "userId": 1
        }),
                         headers=headers,
                         name="Create a new post")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior

