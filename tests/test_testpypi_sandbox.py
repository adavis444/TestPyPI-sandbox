import contextlib
import io

import testpypi_sandbox


def test_get_message() -> None:
    expected = "Welcome to TestPyPI_sandbox!"
    actual = testpypi_sandbox.get_message()
    assert actual == expected


def test_print_message() -> None:
    expected = "Welcome to TestPyPI_sandbox!"
    with io.StringIO() as captured_output, contextlib.redirect_stdout(captured_output):
        testpypi_sandbox.print_message()
        assert captured_output.getvalue().strip() == expected
