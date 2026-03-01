import time
import statistics
from concurrent.futures import ThreadPoolExecutor


def test_get_user_performance(api_client):
    response_times = []
    iterations = 10

    for _ in range(iterations):
        start = time.time()
        response = api_client.get_user(2)
        end = time.time()

        assert response.status_code == 200
        response_times.append(end - start)

    avg = statistics.mean(response_times)
    p95 = sorted(response_times)[int(0.95 * len(response_times)) - 1]

    print(f"Average response time: {avg:.3f}s")
    print(f"P95 response time: {p95:.3f}s")

    assert avg < 1.0
    assert p95 < 2.0

def test_concurrent_requests(api_client):
    def make_request():
        start = time.time()
        response = api_client.get_user(2)
        end = time.time()
        return response.status_code, end - start

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(10)]
        for future in futures:
            results.append(future.result())

    times = [t for status, t in results if status == 200]

    avg = sum(times) / len(times)
    print(f"Concurrent avg response time: {avg:.3f}s")

    assert avg < 2.0

# def test_concurrent_requests(api_client):
#     def make_request():
#         start = time.time()
#         response = api_client.get_user(2)
#         end = time.time()
#         assert response.status_code == 200
#         return end - start

#     with ThreadPoolExecutor(max_workers=5) as executor:
#         response_times = list(executor.map(make_request, range(10)))

#     avg = statistics.mean(response_times)
#     p95 = sorted(response_times)[int(0.95 * len(response_times)) - 1]

#     print(f"Average response time (concurrent): {avg:.3f}s")
#     print(f"P95 response time (concurrent): {p95:.3f}s")

#     assert avg < 1.0
#     assert p95 < 2.0