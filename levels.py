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


COLUMN_HEIGHT = 89 
levels = [
    # Nivel 1 - Introducción básica
    LevelData(
        columns=[(900, 50), (900, 130), (1300, 50)],
        pigs=[(1100, 100)],
    ),
    # Nivel 2 - Dos cerdos protegidos
    LevelData(
        columns=[*add_columns_around_pig(920, 100), *add_columns_around_pig(1200, 100)],
        pigs=[(920, 100), (1200, 100)],
    ),
    # Nivel 3 
    LevelData(
        columns=[
            # Piso 1 
            (900, 50), (950, 50), (1000, 50), (1050, 50), (1100, 50),
            (925, 130, True), (975, 130, True), (1025, 130, True), (1075, 130, True),
            # Piso 2
            (925, 160), (975, 160), (1025, 160), (1075, 160),
            (950, 240, True), (1050, 240, True),
            # Piso 3 
            (950, 270), (1050, 270),
            (1000, 350, True)
        ],
        pigs=[(925, 80), (975, 80), (1025, 80), (1075, 80), (950, 200), (1050, 200), (1000, 310)],
    ),
    # Nivel 4 
    LevelData(
        columns=[
            # Torres de entrada
            (700, 50), (750, 50), (1200, 50), (1250, 50),
            (725, 130, True), (1225, 130, True),
            # Muralla principal con compartimentos
            (850, 50), (900, 50), (950, 50), (1000, 50), (1050, 50), (1100, 50),
            (875, 130, True), (925, 130, True), (975, 130, True), (1025, 130, True), (1075, 130, True)
        ],
        pigs=[(725, 80), (875, 80), (925, 80), (975, 80), (1025, 80), (1075, 80), (1225, 80)],
    ),
    # Nivel 5 
    LevelData(
        columns=[
            # Centro
            (950, 50), (1050, 50), (1000, 130, True),
            # Primera vuelta
            (900, 100), (1100, 100), (950, 180, True), (1050, 180, True),
            # Segunda vuelta
            (850, 150), (1150, 150), (900, 230, True), (1100, 230, True),
            # Tercera vuelta exterior
            (800, 200), (1200, 200)
        ],
        pigs=[(1000, 80), (950, 140), (1050, 140), (900, 190), (1100, 190), (850, 240), (1200, 240)],
    ),
    # Nivel 6 
    LevelData(
        columns=[
            # Centro de la estrella
            (950, 50), (1050, 50), (1000, 130, True),
            # Brazo superior
            (1000, 160), (975, 240, True), (1025, 240, True),
            # Brazo inferior derecho
            (1100, 100), (1150, 50), (1125, 130, True),
            # Brazo inferior izquierdo
            (900, 100), (850, 50), (875, 130, True),
            # Brazos laterales
            (800, 130), (1200, 130)
        ],
        pigs=[(1000, 80), (1000, 200), (1125, 80), (875, 80), (800, 160), (1200, 160)],
    ),
    # Nivel 7 
    LevelData(
        columns=[
            # Anillo exterior
            (700, 100), (750, 80), (850, 60), (950, 50), (1050, 50), (1150, 60), (1250, 80), (1300, 100),
            (725, 180, True), (875, 140, True), (1000, 130, True), (1125, 140, True), (1275, 180, True),
            # Anillo interior
            (900, 130), (1100, 130), (950, 210, True), (1050, 210, True)
        ],
        pigs=[(750, 120), (900, 80), (1000, 80), (1100, 80), (1250, 120), (950, 170), (1050, 170)],
    ),
    # Nivel 8 
    LevelData(
        columns=[
            *add_columns_around_pig(800, 100),
            *add_columns_around_pig(1100, 150),
            (950, 50), (950, 130), (950, 210)
        ],
        pigs=[(800, 100), (1100, 150), (950, 240)],
    ),
    # Nivel 9 
    LevelData(
        columns=[
            # Primera línea zigzag (izquierda alta, derecha baja)
            (700, 100), (750, 50), (775, 130, True),
            (850, 50), (900, 100), (875, 130, True),
            # Segunda línea zigzag (invertida)
            (1000, 100), (1050, 50), (1025, 130, True),
            (1150, 50), (1200, 100), (1175, 130, True)
        ],
        pigs=[(725, 80), (875, 80), (1025, 80), (1175, 80), (700, 140), (1200, 140)],
    ),
    # Nivel 10 
    LevelData(
        columns=[
            # Lado izquierdo del corazón
            (800, 80), (850, 50), (900, 80), (825, 160, True), (875, 160, True),
            (850, 190), (825, 270, True),
            # Lado derecho del corazón
            (1100, 80), (1150, 50), (1200, 80), (1125, 160, True), (1175, 160, True),
            (1150, 190), (1175, 270, True),
            # Centro del corazón
            (950, 120), (1050, 120), (1000, 200, True),
            (1000, 230)
        ],
        pigs=[(825, 120), (875, 120), (950, 80), (1050, 80), (1125, 120), (1175, 120), (1000, 160), (850, 230), (1150, 230), (1000, 270)],
    ),
    # Nivel 11 
    LevelData(
        columns=[
            # Base amplia 
            (500, 50), (550, 50), (600, 50), (650, 50), (700, 50), (750, 50), (800, 50), (850, 50), 
            (900, 50), (950, 50), (1000, 50), (1050, 50), (1100, 50), (1150, 50), (1200, 50), (1250, 50), (1300, 50),
            # Vigas horizontales a altura segura para crear techos
            (525, 130, True), (625, 130, True), (725, 130, True), (825, 130, True), (925, 130, True), 
            (1025, 130, True), (1125, 130, True), (1225, 130, True), (1275, 130, True)
        ],
        pigs=[(525, 80), (625, 80), (725, 80), (825, 80), (925, 80), (1025, 80), (1125, 80), (1225, 80), (1275, 80)],
    ),
]
