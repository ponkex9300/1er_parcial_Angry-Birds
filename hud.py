import arcade

class GameHUD:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self, score):
        arcade.draw_text(
            f"Score: {score}", 
            20, 
            self.height - 40, 
            arcade.color.AERO_BLUE, 
            font_size=25
        )
