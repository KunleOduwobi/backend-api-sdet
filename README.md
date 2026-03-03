# 🚀 Backend API Test Automation Framework (Python + pytest)

## 📌 Overview

This project is a production-style Backend API Test Automation Framework built using:

- Python 3
- pytest
- requests
- jsonschema
- SQLAlchemy
- GitHub Actions (CI)
- Allure + JUnit reporting

It demonstrates modern Backend SDET practices including:

- Clean API client abstraction
- Authentication handling
- Payload builders
- Schema & contract validation
- Async API polling
- Database validation
- Performance checks
- Test categorization (smoke / regression / performance / mocked)
- CI/CD integration with secure secret handling

---

# 🏗 Architecture
backend-api-sdet/
│
├── app/
│ ├── api_client.py # Reusable API client (auth, retries, headers)
│ ├── payloads.py # Payload builders
│ ├── validators.py # Response & contract validators
│ ├── schemas.py # JSON schemas
│ ├── contracts.py # Consumer contract definitions
│ ├── polling.py # Async polling utility
│ └── db_client.py # Database validation client
│
├── tests/
│ ├── conftest.py # Fixtures (API client, setup)
│ ├── test_api.py
│ ├── test_auth.py
│ ├── test_async_api.py
│ ├── test_contracts.py
│ ├── test_performance.py
│ └── test_api_mocked.py
│
├── .github/workflows/ # CI pipelines (smoke + nightly regression)
├── pytest.ini # Marker configuration
├── requirements.txt
└── README.md


---

# 🧪 Test Strategy

Tests are grouped using pytest markers:

| Marker | Purpose | CI Usage |
|--------|----------|----------|
| `smoke` | Critical API validation | Run on every PR |
| `regression` | Full functional coverage | Nightly |
| `performance` | Basic latency checks | On demand |
| `mocked` | Deterministic HTTP mocking | Local/CI |

### Run specific test types:

```bash
python3 -m pytest -m smoke
python3 -m pytest -m "not performance"
python3 -m pytest -m mocked
```

---

# 🔐 Authentication Handling

- API keys injected via environment variables
- Secrets managed in GitHub Actions
- No hardcoded credentials
- Centralized auth logic inside APIClient

Example:

`self.headers["Authorization"] = f"Bearer {token}"`

---

# 🔄 Async API Testing

Async endpoints are handled using a polling utility instead of fixed sleeps:

`poll_until(action, condition, timeout=10, interval=1)`
This avoids flaky tests and supports eventual consistency.

---

# 📦 Contract & Schema Validation
- JSON Schema validation using jsonschema
- Consumer-driven contract definitions
- Breaking-change detection built into CI

Contract tests protect consumers from incompatible API changes.

---

# 🗄 Database Validation

- SQLAlchemy-based DB client
- Validates API response against database state
- Supports SQLite locally
- Environment-variable based DB configuration
- Designed to extend to Postgres/MySQL

Example use case:
Validate that API response data matches DB record.

---

# ⚡ Performance Checks
Lightweight performance validation includes:
- Average response time
- P95 latency calculation
- Concurrent request simulation
- Early regression detection

Not intended to replace full load testing tools.

---

# 🧰 Mocking External APIs
Uses responses library to mock HTTP requests for:
- Deterministic testing
- Edge case simulation
- Faster execution
- Reduced dependency on external services

---

# 📊 Test Reporting
Supports:
- JUnit XML (CI systems)
- pytest-html (human-readable reports)
- Allure results (advanced reporting)

Generate locally:
```bash
python -m pytest -m smoke \
  --junitxml=reports/junit.xml \
  --html=reports/report.html \
  --self-contained-html
  ```
  Allure:
  ```bash
  python -m pytest --alluredir=allure-results
  allure serve allure-results
  ```

---

# 🔁 CI/CD Integration
GitHub Actions:
- Smoke tests on every PR
- Nightly regression workflow
- Secrets handled securely
- Reports uploaded as CI artifacts
- Optional Slack notifications
- Optional Allure publishing

---

# 🔒 Environment Configuration
Secrets are injected via:
```bash
export REQRES_API_KEY=your_key
```

or GitHub Secrets.
Dependencies are pinned using:
```bash
pip freeze > requirements.txt
```
Ensures reproducible CI builds.