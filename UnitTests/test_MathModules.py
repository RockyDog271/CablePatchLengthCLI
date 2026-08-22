from Modules.MathModules import cable_length_calc
from Modules.MathModules import distance_math_function

# Unit tests for the "cable_length_calc" are inside of this class
class TestCableLengthCalc:
    # This tests the expected output for the expected input
    def test_cable_length_normal(self):
        result = cable_length_calc(
            min_bend_radius = 1.00,
            max_bend_radius = 3.00,
            connector_size = 1.75,
            slack_cutoff = 2.00,
            point_to_point_dist = 7.4
        )
        assert result == 15.4

    # This tests the output when the bend radius is smaller than expected
    def test_cable_length_small_bend_radius(self):
        result = cable_length_calc(
            min_bend_radius = 0.25,
            max_bend_radius = 30,
            connector_size = 0.5,
            slack_cutoff = 2.50,
            point_to_point_dist = 10
        )
        assert result == 25.5

    # This tests the output when the bend radius is much larger than what might be expected
    def test_cable_length_large_bend_radius(self):
        result = cable_length_calc(
            min_bend_radius = 10,
            max_bend_radius = 12,
            connector_size = 2.3,
            slack_cutoff = 5,
            point_to_point_dist = 10
        )
        assert result == 28.1

    # This tests the output when the inputs are overly precise
    def test_cable_length_decimal_values(self):
        result = cable_length_calc(
            min_bend_radius = 1.245,
            max_bend_radius = 5.9005,
            connector_size = 1.456,
            slack_cutoff = 2.5033,
            point_to_point_dist = 10.666666666666667
        )
        assert result == 20.09

    # This tests the output when there is zero(0) slack
    def test_cable_length_zero_slack(self):
        result = cable_length_calc(
            min_bend_radius = 1,
            max_bend_radius = 3,
            connector_size = 1,
            slack_cutoff = 0.00,
            point_to_point_dist = 8
        )
        assert result == 10.5

    # This tests the output with no distance in the patch cable, ie: bluetooth connection lol
    def test_cable_length_zero_distance(self):
        result = cable_length_calc(
            min_bend_radius = 1,
            max_bend_radius = 3,
            connector_size = 1,
            slack_cutoff = 2,
            point_to_point_dist = 0.00
        )
        assert result == 6.5

    # This tests the output when the bend radius is really large?
    def test_cable_length_boundary_bend_radius(self):
        result = cable_length_calc(
            min_bend_radius = 1,
            max_bend_radius = 3,
            connector_size = 1,
            slack_cutoff = 2,
            point_to_point_dist = 60
        )
        assert result == 66.5

    # This has a bunch of decimal places to make sure rounding is properly happening
    def test_cable_length_rounding(self):
        result = cable_length_calc(
            min_bend_radius = 1.0000001,
            max_bend_radius = 3.0000001,
            connector_size = 1.0000001,
            slack_cutoff = 2.0000001,
            point_to_point_dist = 10.0000001
        )
        assert result == 16.5

# Unit tests for the "distance_math_function" are inside of this class
class TestDistanceMathFunction:
    # The expected inputs within expected ranged
    def test_distance_math_function_normal(self, capsys):
        result = distance_math_function(
            u_height = 4,
            patch_port_position = "middle",
            device_port_position = "middle",
            port_distance = 4,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "horizontal_distance" in captured.out # Ensure debug printed the name of the variable
        assert "7.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out     # Ensure debug printed that it was from debug
        assert "vertical_distance" in captured.out   # Ensure debug printed the name of the variable
        assert "2.0" in captured.out                # Ensure debug printed the correct value of the variable

        assert result == 8.93                       # The output of the function

    # Testing that the output is correct with small outputs
    def test_distance_math_function_small(self, capsys):
        result = distance_math_function(
            u_height = 2,
            patch_port_position = "bottom",
            device_port_position = "top",
            port_distance = 0,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out      # Ensure debug printed that it was from debug
        assert "horizontal_distance" in captured.out # Ensure debug printed the name of the variable
        assert "3.5" in captured.out                 # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out      # Ensure debug printed that it was from debug
        assert "vertical_distance" in captured.out   # Ensure debug printed the name of the variable
        assert "0.0" in captured.out                 # Ensure debug printed the correct value of the variable

        assert result == 3.00                        # The output of the function

    # Testing that the output is correct with small outputs
    def test_distance_math_function_large(self, capsys):
        result = distance_math_function(
            u_height = 42,
            patch_port_position = "top",
            device_port_position = "bottom",
            port_distance = 16,
            debug = 1
        )
        captured = capsys.readouterr()

        assert "DEBUG PRINTOUT" in captured.out      # Ensure debug printed that it was from debug
        assert "horizontal_distance" in captured.out # Ensure debug printed the name of the variable
        assert "73.5" in captured.out                # Ensure debug printed the correct value of the variable

        assert "DEBUG PRINTOUT" in captured.out      # Ensure debug printed that it was from debug
        assert "vertical_distance" in captured.out   # Ensure debug printed the name of the variable
        assert "8.0" in captured.out                 # Ensure debug printed the correct value of the variable

        assert result == 73.44                       # The output of the function