from manim import *
from manim_chemtex import ChemTex, ChemArrow

class Phthalocyanine(Scene):
    def construct(self):
        self.wait(2)

        struct_phthalic_anhydride = ChemTex(r"\chemfig{*6(=-*5(-(=O)-O-(=O)-)=-=-)}", font_size=25)
        text_phtalic_anhydride = Tex("Phthalic anhydride", font_size=25).shift([0,-2,0])
        PhthalicAnhydride = VGroup(
            struct_phthalic_anhydride, text_phtalic_anhydride
            ).shift([-5,0,0])

        plus_1 = Tex(
            r"+"
            ).shift([-3,0,0])

        struct_urea = ChemTex(r"\chemfig{H-[:-30]N(-[:-90]H)-[:30]C(=[:90]O)-[:-30]N(-[:-90]H)-[:30]H}", font_size=25)
        text_urea = Tex("Urea", font_size=25).shift([0,-2,0])
        Urea = VGroup(
            struct_urea,text_urea
            ).shift([-1,0,0])
        
        plus_2 = Tex(
            r"+"
            ).shift([1,0,0])
        
        struct_CuCl = ChemTex(r"\chemfig{CuCl}", font_size=25).shift([2,0,0])

        ce_arrow = ChemArrow([2.5,0,0], [6,0,0])
        arrow_above_text = ce_arrow.above_obj("ammonium molybdate (cat.)",font_size=20)
        arrow_below_text = ce_arrow.below_obj(r"180-200\,\si{\celsius}",font_size=20)

        self.play(Write(PhthalicAnhydride))
        self.play(Write(plus_1))
        self.play(Write(Urea))
        self.play(Write(plus_2))
        self.play(Write(struct_CuCl))
        self.play(Write(ce_arrow))
        self.play(Write(arrow_above_text))
        self.play(Write(arrow_below_text))

        reaction_formula = VGroup(
            PhthalicAnhydride, 
            plus_1, 
            Urea, 
            plus_2, 
            struct_CuCl, 
            ce_arrow, 
            arrow_above_text, 
            arrow_below_text
            )
        self.wait(1)

        self.play(
            reaction_formula.animate.scale(0.5).shift([-3,3,0])
            )

        struct_Pc = ChemTex(r"\chemfig{N?[a]=[::+63]*5(-N?[b]=(-N=[::-54]*5(-N?[c]=(-N=[::-54]*5(-N?[d]=(-N=[::-54]*5(-N(-[::-54,1.5]Cu?[b,,dotted]?[c]?[d,,dotted])=[,,1]?[a]-(*6(=-=-=-))--))-(*6(=-=-=-))--))-(*6(=-=-=-))--))-(*6(=-=-=-))--)}", font_size=25)
        struct_Pc.shift([1.5,-1,0])
        text_Pc = Tex("Phthalocyanine", font_size=30).shift([1.5,2,0])
        phthalocyanine = VGroup(
            struct_Pc, text_Pc
        )
        
        self.play(Write(phthalocyanine))
        self.wait(2)

        self.play(phthalocyanine.animate.set_color("#757EFA"))
        self.wait(3)