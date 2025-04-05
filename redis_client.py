# redis_client.py
import redis

# Initialize the Redis connection once
r = redis.Redis(host='localhost', port=6379, db=0)
