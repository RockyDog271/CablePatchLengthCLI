from Modules.MathModules import cable_length_calc
from Modules.MathModules import distance_math_function

# Unit tests for the "cable_length_calc" are inside of this class
class TestCableLengthCalc:
    # This tests the expected output for the expected input
    def test_cable_length_normal(self):
        result = cable_length_calc(
            minBendRadius = 1.00,
            maxBendRadius = 3.00,
            connectorSize = 1.75,
            slackCutoff = 2.00,
            pointToPointDist = 7.4
        )
        assert result == 15.4

    # This tests the output when the bend radius is smaller than expected
    def test_cable_length_small_bend_radius(self):
        result = cable_length_calc(
            minBendRadius = 0.25,
            maxBendRadius = 30,
            connectorSize = 0.5,
            slackCutoff = 2.50,
            pointToPointDist = 10
        )
        assert result == 25.5

    # This tests the output when the bend radius is much larger than what might be expected
    def test_cable_length_large_bend_radius(self):
        result = cable_length_calc(
            minBendRadius = 10,
            maxBendRadius = 12,
            connectorSize = 2.3,
            slackCutoff = 5,
            pointToPointDist = 10
        )
        assert result == 28.1

    # This tests the output when the inputs are overly precise
    def test_cable_length_decimal_values(self):
        result = cable_length_calc(
            minBendRadius = 1.245,
            maxBendRadius = 5.9005,
            connectorSize = 1.456,
            slackCutoff = 2.5033,
            pointToPointDist = 10.666666666666667
        )
        assert result == 20.09

    # This tests the output when there is zero(0) slack
    def test_cable_length_zero_slack(self):
        result = cable_length_calc(
            minBendRadius = 1,
            maxBendRadius = 3,
            connectorSize = 1,
            slackCutoff = 0.00,
            pointToPointDist = 8
        )
        assert result == 10.5

    # This tests the output with no distance in the patch cable, ie: bluetooth connection lol
    def test_cable_length_zero_distance(self):
        result = cable_length_calc(
            minBendRadius = 1,
            maxBendRadius = 3,
            connectorSize = 1,
            slackCutoff = 2,
            pointToPointDist = 0.00
        )
        assert result == 6.5

    # This tests the output when the bend radius is really large?
    def test_cable_length_boundary_bend_radius(self):
        result = cable_length_calc(
            minBendRadius = 1,
            maxBendRadius = 3,
            connectorSize = 1,
            slackCutoff = 2,
            pointToPointDist = 60
        )
        assert result == 66.5

    # This has a bunch of decimal places to make sure rounding is properly happening
    def test_cable_length_rounding(self):
        result = cable_length_calc(
            minBendRadius = 1.0000001,
            maxBendRadius = 3.0000001,
            connectorSize = 1.0000001,
            slackCutoff = 2.0000001,
            pointToPointDist = 10.0000001
        )
        assert result == 16.5

    # A minimum bend radius of exactly 1.5 should not receive the small-radius adjustment
    def test_cable_length_bend_radius_threshold(self):
        result = cable_length_calc(
            minBendRadius = 1.5,
            maxBendRadius = 6,
            connectorSize = 1,
            slackCutoff = 0,
            pointToPointDist = 0
        )
        assert result == 3.5

# Unit tests for the "distance_math_function" are inside of this class
class TestDistanceMathFunction:
    # The expected inputs within expected ranged
    def test_distance_math_function_normal(self, capsys):
        result = distance_math_function(
            uHeight = 4,
            patchPortPosition = "middle",
            devicePortPosition = "middle",
            portDistance = 4,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "horizontalDistance" in captured.out # Ensure debug printed the name of the variable
        assert "7.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "verticalDistance" in captured.out   # Ensure debug printed the name of the variable
        assert "2.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert result == 8.93                       # The output of the function

    # Testing that the output is correct with small outputs
    def test_distance_math_function_small(self, capsys):
        result = distance_math_function(
            uHeight = 2,
            patchPortPosition = "bottom",
            devicePortPosition = "top",
            portDistance = 0,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "horizontalDistance" in captured.out # Ensure debug printed the name of the variable
        assert "3.5" in captured.out                # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "verticalDistance" in captured.out   # Ensure debug printed the name of the variable
        assert "0.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert result == 3.00                       # The output of the function

    # Testing that the output is correct with small outputs
    def test_distance_math_function_large(self, capsys):
        result = distance_math_function(
            uHeight = 42,
            patchPortPosition = "top",
            devicePortPosition = "bottom",
            portDistance = 16,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "horizontalDistance" in captured.out # Ensure debug printed the name of the variable
        assert "73.5" in captured.out                # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "verticalDistance" in captured.out   # Ensure debug printed the name of the variable
        assert "8.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert result == 73.44                      # The output of the function

    # A zero-height rack still has distance between two top ports because of their offsets
    def test_distance_math_function_zero_height_top_ports(self):
        result = distance_math_function(
            uHeight = 0,
            patchPortPosition = "top",
            devicePortPosition = "top",
            portDistance = 0,
            debug = 0
        )
        assert result == 1.5
