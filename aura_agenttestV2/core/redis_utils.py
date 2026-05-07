import redis

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host="127.0.0.1",
            port=6379,
            db=0,
            decode_responses=True
        )

    def set(self, key, value, ex=3600):
        self.client.set(key, value, ex=ex)

    def get(self, key):
        return self.client.get(key)