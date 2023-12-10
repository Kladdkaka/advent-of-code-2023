from pathlib import Path
from operator import mul
import functools


def get_max_boxes(rounds):
  colors = {
    'red': 0,
    'green': 0,
    'blue': 0
  }

  for round in rounds:
    for color, num in round.items():
      if num > colors[color]:
        colors[color] = num
  
  return colors


def parse_line(line: str):
  game, rounds = line.split(': ')
  game = int(game.removeprefix('Game '))
  rounds = [{r.split(' ')[1]: int(r.split(' ')[0]) for r in round.split(', ')} for round in rounds.split('; ')]
  return game, rounds

if __name__ == "__main__":
  p = Path(__file__).parent / 'input.txt'
  lines = p.read_text().splitlines()
  
  games = [parse_line(line) for line in lines]

  eligible_games = []
  powers = []
  for game, rounds in games:
    colors = get_max_boxes(rounds)

    if colors['red'] <= 12 and colors['green'] <= 13 and colors['blue'] <= 14:
      print('match for game ', game)
      eligible_games.append(game)
    
    powers.append(functools.reduce(mul, (x if x >= 1 else 1 for x in colors.values()), 1))

  print('game sum', sum(eligible_games))
  print('powers sum', sum(powers))