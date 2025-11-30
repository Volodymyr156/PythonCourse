import simple_math
SMtest = simple_math.SimpleMath()
try:
    """Several tests with cube and square method"""
    assert SMtest.cube(1032323) == 1032323 ** 3
    print("SMtest.cube:", SMtest.cube(1032323), "| Using usual ** operand:", 1032323 ** 3)
    print("Equal?", SMtest.cube(1032323) == 1032323 ** 3,"\n-----------------------------------------------------------------------------")

    assert SMtest.cube(0) == 0
    print("SMtest.cube:", SMtest.cube(0), "| Using usual ** operand:", 0 ** 3)
    print("Equal?", SMtest.cube(0) == 0 ** 3, "\n-----------------------------------------------------------------------------")

    assert SMtest.cube(-25) == -25 ** 3
    print("SMtest.cube:", SMtest.cube(-25), "| Using usual ** operand:", -25 ** 3)
    print("Equal?", SMtest.cube(-25) == -25 ** 3, "\n-----------------------------------------------------------------------------")

    assert SMtest.square(1032323) == 1032323 * 1032323
    print("SMtest.square:", SMtest.square(1032323), "| Using usual ** operand:", 1032323 ** 2)
    print("Equal?", SMtest.square(1032323) == 1032323 ** 2,"\n-----------------------------------------------------------------------------")

    assert SMtest.square(0) == 0
    print("SMtest.square:", SMtest.square(0), "| Using usual ** operand:", 0 ** 2)
    print("Equal?", SMtest.square(0) == 0 ** 2,"\n-----------------------------------------------------------------------------")

    assert SMtest.square(-25) == -25 ** 2
    print("SMtest.square:", SMtest.square(-25), "| Using usual ** operand:", -25 ** 2)
    print("Equal?", SMtest.square(-25) == -25 ** 2,"\n-----------------------------------------------------------------------------")


    print("Test was successfully ended")
except AssertionError:
    print("Test was not successfully ended")
