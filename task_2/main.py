import re
from typing import Callable

def generator_numbers(text: str):
	"""
	Generator that yields numbers from a text
	text: str - input text
	"""
	pattern = r"^\d*[.]?\d*$"
	for part in text.split(' '):
		if re.match(pattern, part):
			yield float(part)

def sum_profit(text: str, func: Callable) -> float:
	"""
	Sum all numbers from a text
	text: str - input text
	func: Callable - generator function
	"""
	return sum(func(text))

def main() -> None:
	text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
	total_income = sum_profit(text, generator_numbers)
	print(f"Загальний дохід: {total_income}")
	
if __name__ == "__main__":
	main()