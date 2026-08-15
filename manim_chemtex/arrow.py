from manim import *

class ChemArrow(VGroup):
    TEMPLATE = TexTemplate()
    TEMPLATE.add_to_preamble(r"\usepackage{chemfig}")
    TEMPLATE.add_to_preamble(r"\usepackage[version=4]{mhchem}")
    TEMPLATE.add_to_preamble(r"\usepackage{siunitx}")
    def __init__(self, start, end, **kwargs):
        super().__init__(**kwargs)
        self.template = self.TEMPLATE

        self.chem_arrow = Arrow(
            start,
            end,
            tip_shape=StealthTip,
            stroke_width=1,
        )
        self.chem_arrow.tip.scale(0.3)

        self.add(self.chem_arrow)

    def above_obj(self, tex, buff=0.15, **kwargs):
        obj = Tex(
            tex,
            tex_template=self.template,
            **kwargs,
        )
        obj.next_to(self.chem_arrow, UP, buff=buff)
        return obj

    def below_obj(self, tex, buff=0.15, **kwargs):
        obj = Tex(
            tex,
            tex_template=self.template,
            **kwargs,
        )
        obj.next_to(self.chem_arrow, DOWN, buff=buff)
        return obj