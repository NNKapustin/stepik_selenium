## test_fixture.py - classical fixtures. First class browser launch once for all tests, not stable but faster. Second each test in separate launch of browser, longer, but more stable. launch ***pytest -s test_fixture1.py***
## test_fixture2.py - fixtures with return value by @pytest.fixture launch ***pytest -s -v test_fixture2.py***
## test_fixture3.py - finalization by using yield, and scopes