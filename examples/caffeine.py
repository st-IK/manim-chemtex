from manim import *
from manim_chemtex import ChemTex, ChemArrow

class Caffeine(Scene):
    def construct(self):

        caffeine = ChemTex(
            r"\chemfig{N*5(-C(=O)-N(-CH_3)-C(=O)-N(-CH_3)-C(-H)=)}",
            font_size=40,
        )

        caffeine.set_bond_stroke(width=2)

        caffeine.set_bond_color(0, RED)
        caffeine.set_bond_color(1, BLUE)

        self.play(Write(caffeine))
        self.wait(2)

        text = Tex(r"Caffein")
        text.shift(UP*2)

        self.play(
            caffeine.animate.shift(DOWN),
            Write(text)
            )
        
        self.wait(3)