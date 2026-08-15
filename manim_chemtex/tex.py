from manim import *

class ChemTex(VGroup):
    TEMPLATE = TexTemplate()
    TEMPLATE.add_to_preamble(r"\usepackage{chemfig}")
    TEMPLATE.add_to_preamble(r"\usepackage[version=4]{mhchem}")
    TEMPLATE.add_to_preamble(r"\usepackage{siunitx}")
    def __init__(self, src=None, **kwargs):
        super().__init__()
        self.template = self.TEMPLATE
        if src is not None:
            self.chem_tex(src, **kwargs)

    def _get_bonds(self):
        members = self.family_members_with_points()

        #=====================================================================================
        # Bond objects are detected heuristically from Manim's vectorized SVG representation.
        #=====================================================================================
        return [
            sm for sm in members
            if sm.get_fill_opacity() == 0
            and sm.get_num_points() == 4
        ]

    def set_bond_stroke(self, width=1):
        for bond in self._get_bonds():
            bond.set_stroke(width=width)

    def set_bond_color(self, bond_num, color):
        bonds = self._get_bonds()

        if bond_num >= len(bonds):
            raise IndexError("bond_num が範囲外です")

        bonds[bond_num].set_color(color)

    def chem_tex(self, src, **kwargs):
        tex = Tex(
            src,
            tex_template=self.template,
            **kwargs
        )

        self.add(tex)

        self.parts = self.family_members_with_points()
        self.set_bond_stroke()

        return self