from recursive import summation
from decisions import compare_number_thresh

# test summation
assert summation(2) == 3
assert summation(3) == 6
assert summation(4) == 10
assert summation(55) == 1540
assert summation('55') == 1540
assert summation('5b5') == 0

# test compare_number_thresh
assert compare_number_thresh(0, 10).lower().strip() == "Small Number".lower().strip()
assert compare_number_thresh(10, 0).lower().strip() == "big Number".lower().strip()
assert compare_number_thresh(0, 0).lower().strip() == "number is 0".lower().strip()