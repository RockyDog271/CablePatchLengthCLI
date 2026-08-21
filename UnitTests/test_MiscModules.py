# from Modules.Scripts import data_input_script
from Modules.DebugModule import debug_printout
from Modules.DebugModule import debug_exception
from Modules.DebugModule import debug_value_printout

# Unit tests for the "input_loop" are inside of this class
class TestDebugPrintout:
    pass

# Unit tests for the "input_loop" are inside of this class
class TestDebugException:
    def test_debug_exception_basic(self, capsys):
        try:
            raise ValueError("Test Exception")
        except ValueError as exception:
            debug_exception(2, exception)

        captured = capsys.readouterr()
        assert "Test Exception" in captured.out
        assert "ValueError" in captured.out

# Unit tests for the "input_loop" are inside of this class
class TestDebugValuePrintout:
    pass

# Unit tests for the "input_loop" are inside of this class
class TestDataInputScript:
    pass
   # Like... V0.5? maybe I'll make this in V0.4? same time as test_CLI probs