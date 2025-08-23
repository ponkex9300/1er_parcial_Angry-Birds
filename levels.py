from dataclasses import dataclass
from typing import List, Tuple


def add_columns_around_pig(pig_x, pig_y):
    return [
        (pig_x - 20, pig_y - 50),
        (pig_x + 30, pig_y - 50),
        (pig_x + 5, pig_y + 50, True),
    ]


@dataclass
class LevelData:
    columns: List[Tuple[float, float, bool]]
    pigs: List[Tuple[float, float]]


COLUMN_HEIGHT =89 
levels = [
    LevelData(
        columns=[(900, 50), (900, 130), (1300, 50)],
        pigs=[(1100, 100)],
    ),
    LevelData(
        columns=[*add_columns_around_pig(920, 100), *add_columns_around_pig(1200, 100)],
        pigs=[(920, 100), (1200, 100)],
    )
]
