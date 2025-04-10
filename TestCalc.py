#!/usr/bin/python

import sys, Calc

SystemTests = [
	("single",    "45",            "45"),
	("basic",     "1 + 2 * 3",     "7" ),
	("parenth",   "(1 + 2) * 3",   "9" ),
]

def run_system_tests():
	Calc.setup()

	failures = 0
	for (name, line, expected) in SystemTests:
		number = Calc.parse(line)
		actual = str(number)
		if expected != actual:
			print("FAIL '%s' expected '%s' saw '%s'" % (name, expected, actual))
			failures += 1
	return failures

def main():
	failures = 0
	failures += run_system_tests()
	return failures

if __name__ == "__main__":
	sys.exit(main())

