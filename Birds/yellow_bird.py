import pymunk
from game_logic import ImpulseVector, Point2D, get_impulse_vector
from game_object import Bird


class YellowBird(Bird):
    def __init__(
        self,
        image_path: str,
        scale: float,
        impulse_vector: ImpulseVector,
        x: float,
        y: float,
        space: pymunk.Space,
        mass: float = 5,
        radius: float = 12,
        max_impulse: float = 100,
        power_multiplier: float = 50,
        elasticity: float = 0.8,
        friction: float = 1,
        collision_layer: int = 0,
        boost_multiplier: float = 3.0,
    ):
        super().__init__(
            image_path,
            scale,
            impulse_vector,
            x,
            y,
            space,
            mass,
            radius,
            max_impulse,
            power_multiplier,
            elasticity,
            friction,
            collision_layer,
        )
        self.boost_multiplier = boost_multiplier
        self.is_boosted = False

    def update(self, delta_time: float = 1/60):
        super().update(delta_time)
        if self.is_boosted:
            impulse_vector = get_impulse_vector(
                Point2D(0, 0),
                Point2D(self.center_x, self.center_y),
            )
            impulse_vector.impulse *= self.boost_multiplier
            self.body.apply_impulse_at_local_point(
                impulse_vector.impulse
                * pymunk.Vec2d(1, 0).rotated(impulse_vector.angle)
            )

    def power_up(self):
        self.is_boosted = True
        self.update()
