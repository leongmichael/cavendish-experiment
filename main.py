from manim import *

config.media_width = "100%"
config.verbosity = "WARNING"



# animation 1
class displayNewtonsLaws(Scene):
    def construct(self):
        newtonSecondLaw = MathTex(r"F=ma")
        newtonSecondLaw.shift(UP * 1.5)
        self.play(Create(newtonSecondLaw))
        self.wait(2)
        newtonLawRotationalMotion = MathTex(r"\tau=rf")
        newtonLawRotationalMotion.next_to(newtonSecondLaw, DOWN)
        self.play(Create(newtonLawRotationalMotion))
        self.wait(2)
        newtonUniversalGravitation = MathTex(r"F=G\frac{m_1m_2}{r^2}")
        newtonUniversalGravitation.next_to(newtonLawRotationalMotion, DOWN)
        self.play(Create(newtonUniversalGravitation))


# animation 2
class deriveGMe(Scene):
    def construct(self):
        newtonSecondLaw = MathTex(r"F=mg")
        newtonSecondLaw.shift(UP * 1.5)
        self.play(Create(newtonSecondLaw))
        self.wait(2)
        newtonUniversalGravitation = MathTex(r"F=G\frac{m_{earth}m}{r_{earth}^2}")
        newtonUniversalGravitation.next_to(newtonSecondLaw, DOWN)
        self.play(Create(newtonUniversalGravitation))
        self.wait(2)

        self.play(FadeOut(newtonSecondLaw), FadeOut(newtonUniversalGravitation))
        self.wait(1)

        equate = MathTex(r"mg=G\frac{m_{earth}m}{r_{earth}^2}")
        self.play(Create(equate))
        self.wait(2)

        solveForGMe = MathTex(r"G{m_{earth}={r_{earth}^2}g")
        self.play(TransformMatchingTex(equate, solveForGMe))
        self.wait(1)

