from pathlib import Path
from string import digits

def parse_calibration_value(s: str) -> int:
  first_digit = next(c for c in s if c in digits)
  last_digit = next(c for c in s[::-1] if c in digits)

  assert not (first_digit is None or last_digit is None)
  
  calibration_value = f'{first_digit}{last_digit}'

  return int(calibration_value)

if __name__ == "__main__":
  p = Path(__file__).parent / 'input'
  lines = p.read_text().splitlines()
  
  print(sum(parse_calibration_value(line) for line in lines))