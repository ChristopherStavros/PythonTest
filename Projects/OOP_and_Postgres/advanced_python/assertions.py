def divide_secure(number, divisor):
    # if divisor == 0:
    #     raise ValueError("The divisor is 0")
    assert divisor != 0  # better when program is running in "High performance mode" -- if you may want to turn them off later to improve performance
    return number / divisor

divide_secure(10, 0)