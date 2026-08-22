# from Modules.Scripts import data_input_script
from Modules.DebugModule import debug_printout
from Modules.DebugModule import debug_exception
from Modules.DebugModule import debug_value_printout

# Unit tests for the "debug_printout" are inside of this class
class TestDebugPrintout:
    # Debug 0 **should** print nothing
    def test_debug_printout_off(self, capsys):
        debug_printout(
            debug = 0,
            value_name="testValue",
            value_printout=123
        )
        captured = capsys.readouterr()
        assert captured.out == ""

    # Debug 1 **should** print
    def test_debug_printout_basic(self, capsys):
        debug_printout(
            debug = 1,
            value_name="testValue",
            value_printout=123
        )
        captured = capsys.readouterr()
        assert "DEBUG PRINTOUT" in captured.out
        assert "testValue" in captured.out
        assert "123" in captured.out

    # Debug 3 **should** print
    def test_debug_printout_advanced(self, capsys):
        debug_printout(
            debug = 3,
            value_name="test_value",
            value_printout=123
        )
        captured = capsys.readouterr()
        assert "DEBUG PRINTOUT" in captured.out
        assert "test_value" in captured.out
        assert "123" in captured.out

# Unit tests for the "debug_exception" are inside of this class
class TestDebugException:

    # Debug 0 **should** print nothing
    def test_debug_exception_off(self, capsys):
        try:
            raise ValueError("Test Exception")
        except ValueError as exception:
            debug_exception(0, exception)

        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""

    # Debug 2 **should** print the exception and traceback
    def test_debug_exception_basic(self, capsys):
        try:
            raise ValueError("Test Exception")
        except ValueError as exception:
            debug_exception(2, exception)

        captured = capsys.readouterr()
        assert "DEBUG PRINTOUT" in captured.out
        assert "Test Exception" in captured.out
        assert "ValueError" in captured.err
        assert "Traceback" in captured.err

    # Debug 3 **should** print the exception and traceback
    def test_debug_exception_advanced(self, capsys):
        try:
            raise ValueError("Test Exception")
        except ValueError as exception:
            debug_exception(3, exception)

        captured = capsys.readouterr()
        assert "DEBUG PRINTOUT" in captured.out
        assert "Test Exception" in captured.out
        assert "ValueError" in captured.err
        assert "Traceback" in captured.err

# Unit tests for the "debug_value_printout" are inside of this class
class TestDebugValuePrintout:

    # Debug 0 **should** print nothing
    def test_debug_value_printout_off(self, capsys):
        input_data = {
            "min_value": 1,
            "max_value": 10
        }
        debug_value_printout(
            debug = 0,
            input_data = input_data
        )
        captured = capsys.readouterr()
        assert captured.out == ""

    # Debug 1 **should** print
    def test_debug_value_printout_basic(self, capsys):
        input_data = {
            "min_value": 1,
            "max_value": 10
        }
        debug_value_printout(
            debug = 1,
            input_data=input_data
        )
        captured = capsys.readouterr()
        assert "MIN" in captured.out
        assert "1" in captured.out
        assert "MAX" in captured.out
        assert "10" in captured.out

    # Debug 3 **should** print
    def test_debug_value_printout_advanced(self, capsys):
        input_data = {
            "min_value": 1,
            "max_value": 10
        }
        debug_value_printout(
            debug = 3,
            input_data=input_data
        )
        captured = capsys.readouterr()
        assert "MIN" in captured.out
        assert "1" in captured.out
        assert "MAX" in captured.out
        assert "10" in captured.out

# Unit tests for the "input_loop" are inside of this class
class TestDataInputScript:
    pass
   # Like... V0.5? maybe I'll make this in V0.4? same time as test_CLI probs