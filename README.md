# Insta tests (Playwright + pytest)

0. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
    
   **On Windows:**
   `.\venv\Scripts\activate`

1. Install dependencies:
   pip install -r requirements.txt

2. Install browsers:
   playwright install

3. Adjust tests/conftest.py:
   - Make sure runner_cmd launches your Flask app on 127.0.0.1:5001
   - Or run your Flask app manually on port 5001 before tests.

4. Run tests:
   pytest tests/test_login.py -q

Notes:
- If your app requires CSRF tokens for POST via fetch, tests should either:
  - Perform login via the HTML form (so CSRF token is present), or
  - Inject authentication cookie/session directly into context (see Playwright context.add_cookies), or
  - Provide the CSRF token to fetch headers (read from login page).
- For debugging, set headless=False in conftest.py to watch browser.
