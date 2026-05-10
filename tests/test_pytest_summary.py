from scripts.pytest_summary import count_results


def test_counts_happy_path():
    output = """
    tests/test_example.py ..Fs
    ========== 1 failed, 2 passed, 1 skipped in 0.12s ==========
    """

    assert count_results(output) == {"passed": 2, "failed": 1, "skipped": 1}


def test_empty_file_returns_zero_counts():
    assert count_results("") == {"passed": 0, "failed": 0, "skipped": 0}


def test_no_failures_found():
    output = "========== 5 passed, 2 skipped in 0.08s =========="

    assert count_results(output) == {"passed": 5, "failed": 0, "skipped": 2}


def test_ignores_non_summary_failure_text():
    output = """
    E AssertionError: expected 1 failed assertion message
    ---------- 3 passed in 0.04s ----------
    """

    assert count_results(output) == {"passed": 3, "failed": 0, "skipped": 0}


def test_ignores_other_pytest_outcomes():
    output = "========== 1 xfailed, 1 xpassed, 4 passed in 0.10s =========="

    assert count_results(output) == {"passed": 4, "failed": 0, "skipped": 0}
