from Modules.FuzzyMatch import fuzzy_loop
from Modules.InputModule import input_loop

# Unit tests for the "input_loop" are inside of this class
class TestInputLoop:
    pass

# Unit tests for the "fuzzy_loop" are inside of this class
class TestFuzzyLoop:
    # Tests for normal input
    def test_fuzzy_loop_normal(self, monkeypatch):
        # monkeypatch is what makes the fake user input... 
        monkeypatch.setattr("builtins.input", lambda _: "ADV")
        result = fuzzy_loop(
            debug = 0,
            optionList = ["ez", "adv"],
            fuzzyData = {
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
            optionList = ["ez", "adv"],
            fuzzyData = {
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
            debug=0,
            optionList=["ez", "adv"],
            fuzzyData={
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
            optionList = ["central", "centralized", "tipper", "centered"],
            fuzzyData = {
                "cutoffValue": 0.8,
                "input": f"Mode"  
            }
        )
        assert result == "centralized"