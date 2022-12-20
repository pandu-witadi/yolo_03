#
# 
from kombu import Connection
from kombu.exceptions import OperationalError


def is_broker_running(broker, retries: int = 3) -> bool:
    try:
        conn = Connection(broker)
        conn.ensure_connection(max_retries=retries)
    except OperationalError as e:
        print("Failed to connect to RabbitMQ instance at %s", broker)
        print(str(e))
        return False
    conn.close()
    return True
