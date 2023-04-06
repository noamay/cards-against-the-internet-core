from enum import Enum
from pathlib import Path
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
CARDS_JSON_LOCATION = Path(PROJECT_ROOT + "/cah-all-compact.json").resolve()
DEFAULT_PACK = [1, 2]


class CardType(Enum):
    WHITE = 0
    BLACK = 1


if __name__ == '__main__':
    print(CARDS_JSON_LOCATION)
