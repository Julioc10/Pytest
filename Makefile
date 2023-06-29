all_tests:
	pytest -m "not ignore"

test_imc:
	pytest -s tests/test_imc.py
