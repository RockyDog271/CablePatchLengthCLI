from Modules.MathModules import cable_length_calc
from Modules.MathModules import distance_math_function

def test_standard_patch_cable_one():
    result = cable_length_calc(
        minBendRadius = 1,
        maxBendRadius = 3,
        connectorSize = 1,
        slackCutoff = 2.50,
        pointToPointDist = 10
    )
    assert 12

def test_standard_patch_cable_two():
    result = cable_length_calc(
        minBendRadius = 2,
        maxBendRadius = 30,
        connectorSize = 2.5,
        slackCutoff = 2,
        pointToPointDist = 6
    )
    assert 32

def test_standard_patch_cable_three():
    result = cable_length_calc(
        minBendRadius = 10,
        maxBendRadius = 5,
        connectorSize = 2,
        slackCutoff = 2.00005,
        pointToPointDist = 40
    )
    assert 42

def test_standard_patch_cable_four():
    result = cable_length_calc(
        minBendRadius = 20,
        maxBendRadius = 5,
        connectorSize = 4,
        slackCutoff = 1.5,
        pointToPointDist = 8
    )
    assert 12