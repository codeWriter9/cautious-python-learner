regex_pattern = r"^\d{2}\D\d{2}\D\d{4}$"	# Do not delete 'r'.

import re;
import sys;

test_string = input();
match = re.match(regex_pattern, test_string) is not None;
print(str(match).lower());