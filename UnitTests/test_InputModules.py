from Modules.FuzzyMatch import fuzzy_loop
from Modules.InputModule import input_loop

# Unit tests for the "input_loop" are inside of this class
class TestInputLoop:
    # This tests the normal input
    def test_input_loop_normal(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "5")
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 10,
                "min_value": 1,
                "input": "Value"
            }
        )
        assert result == 5

    # This tests for decimal handling
    def test_input_loop_decimal_check(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "5.506")
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 10,
                "min_value": 1,
                "input": "Value"
            }
        )
        assert result == 5.51

    # This tests the rounding, ensuring it works correctly
    def test_input_loop_rounding_check(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "5.5067888")
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 10,
                "min_value": 1,
                "input": "Value"
            }
        )
        assert result == 5.51

    # This tests the function when the value is too high
    def test_input_loop_high(self, monkeypatch, capsys):
        inputs = iter(["21", "19"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 20,
                "min_value": 10,
                "input": "Value"
            }
        )
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
        assert "too high" in captured.out
        assert "20" in captured.out
        assert "21" in captured.out
        assert result == 19

    # This tests the function when the value is too low
    def test_input_loop_low(self, monkeypatch, capsys):
        inputs = iter(["3", "10"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 20,
                "min_value": 5,
                "input": "Value"
            }
        )
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
        assert "too low" in captured.out
        assert "3" in captured.out
        assert "5" in captured.out
        assert result == 10

    # This tests the function when invalid data is passed
    def test_input_loop_invalid(self, monkeypatch, capsys):
        inputs = iter(["AE", "19"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 20,
                "min_value": 10,
                "input": "Value"
            }
        )
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
        assert result == 19

    # This tests the exact MAX VAL
    def test_input_loop_max(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "30")
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 30,
                "min_value": 10,
                "input": "Value"
            }
        )
        assert result == 30

    # This tests the exact MIN VAL
    def test_input_loop_min(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "10")
        result = input_loop(
            debug = 0,
            input_data = {
                "max_value": 20,
                "min_value": 10,
                "input": "Value"
            }
        )
        assert result == 10


# Unit tests for the "fuzzy_loop" are inside of this class
class TestFuzzyLoop:
    # Tests for normal input
    def test_fuzzy_loop_normal(self, monkeypatch):
        # monkeypatch is what makes the fake user input... 
        monkeypatch.setattr("builtins.input", lambda _: "ADV")
        result = fuzzy_loop(
            debug = 0,
            option_list = ["ez", "adv"],
            fuzzy_data = {
                "cutoffValue": 0.45,
                "input": f"Mode"  
            }
        )
        assert result == "adv"

    # Tests wild input
    def test_fuzzy_loop_wild(self, monkeypatch, capsys):
        # monkeypatch is what makes the fake user input... 
        inputs = iter(["Asdfkhbbhbhdf", "adv"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = fuzzy_loop(
            debug = 0,
            option_list = ["ez", "adv"],
            fuzzy_data = {
                "cutoffValue": 0.35,
                "input": f"Mode"  
            }
        )
        captured = capsys.readouterr()
        assert result == "adv"
        assert "Invalid input" in captured.out
        assert "ez, adv" in captured.out

    # Tests for strict normal
    def test_fuzzy_loop_strict(self, monkeypatch, capsys):
        # monkeypatch is what makes the fake user input... 
        inputs = iter(["advv", "adv"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = fuzzy_loop(
            debug = 0,
            option_list=["ez", "adv"],
            fuzzy_data={
                "cutoffValue": 1.00,
                "input": "Mode"
            }
        )
        captured = capsys.readouterr()
        assert result == "adv"
        assert "Invalid input" in captured.out
        assert "ez, adv" in captured.out

    # Tests for normal input
    def test_fuzzy_loop_generic(self, monkeypatch):
        # monkeypatch is what makes the fake user input... 
        monkeypatch.setattr("builtins.input", lambda _: "Centralized")
        result = fuzzy_loop(
            debug = 0,
            option_list = ["central", "centralized", "tipper", "centered"],
            fuzzy_data = {
                "cutoffValue": 0.8,
                "input": f"Mode"  
            }
        )
        assert result == "centralized"
 