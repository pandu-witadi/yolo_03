from redis import Redis
from redis.exceptions import ConnectionError


def is_backend_running(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD) -> bool:
    try:
        conn = Redis(
            host=REDIS_HOST,
            port=int(REDIS_PORT),
            db=int(REDIS_DB),
            password=REDIS_PASSWORD
        )
        conn.client_list()  # Must perform an operation to check connection.
    except ConnectionError as e:
        print("Failed to connect to Redis instance at %s", REDIS_HOST)
        print(repr(e))
        return False
    conn.close()
    return True
