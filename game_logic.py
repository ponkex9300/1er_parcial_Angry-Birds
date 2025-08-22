import math
import arcade
import numpy as np
from dataclasses import dataclass
from logging import getLogger

logger = getLogger(__name__)

# Constantes de física
GRAVITY = (0, -981)
ELASTICITY = 0.9
FRICTION = 0.1
MAX_IMPULSE = 981

@dataclass
class ImpulseVector:
    angle: float
    impulse: float


@dataclass
class Point2D:
    x: float = 0
    y: float = 0


def get_angle_radians(point_a: Point2D, point_b: Point2D) -> float:
    dy = point_b.y - point_a.y
    dx = point_b.x - point_a.x
    return math.atan2(dy, dx)


def get_distance(point_a: Point2D, point_b: Point2D) -> float:
    dy = point_b.y - point_a.y
    dx = point_b.x - point_a.x
    return math.sqrt(dx**2 + dy**2)


def get_impulse_vector(start_point: Point2D, end_point: Point2D) -> ImpulseVector:
    distance = get_distance(start_point, end_point)
    angle = get_angle_radians(start_point, end_point)
    # Usar una función más suave para el impulso basada en la distancia
    impulse = min(distance * 5, MAX_IMPULSE)  # Escalar con la gravedad
    return ImpulseVector(angle, impulse)
