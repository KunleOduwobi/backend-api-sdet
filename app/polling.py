import time


def poll_until(
    action,
    condition,
    timeout=10,
    interval=1
):
    """
    Repeatedly performs action() until condition(result) is True
    or timeout is reached.
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        result = action()

        if condition(result):
            return result

        time.sleep(interval)

    raise TimeoutError("Condition not met within timeout")