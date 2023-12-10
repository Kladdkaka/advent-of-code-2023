from pathlib import Path
import string
from typing import Tuple
from operator import itemgetter

# zero is not used, just to make index correct 
digit_names = ['_', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = [*string.digits]

digit_pairs = list(enumerate(digit_names)) + list(enumerate(digits))

print(digit_pairs)

# make this not greedy later
def find_digit(s: str) -> Tuple[int, int]: 
  indexes = []

  for num, digit in digit_pairs:
    for i in range(0, len(s) - len(digit) + 1):
      sub = s[i:i + len(digit)]
      if digit == sub:
        indexes.append((i, num))

  return indexes

def parse_calibration_value(s: str) -> int:
  indexes = find_digit(s)

  _, first_digit = min(indexes, key=itemgetter(0))
  _, last_digit = max(indexes, key=itemgetter(0))

  assert not (first_digit is None or last_digit is None)
  
  calibration_value = f'{first_digit}{last_digit}'

  return int(calibration_value)

if __name__ == "__main__":
  p = Path(__file__).parent / 'input'
  lines = p.read_text().splitlines()
  
  print(sum(parse_calibration_value(line) for line in lines))