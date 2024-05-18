import manim
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

        #experimental
        self.wait(2)
        test = MathTex(r"F=G\frac{m_1m_2}{rrrrr}")
        test.next_to(newtonUniversalGravitation, DOWN)
        self.play(Create(test))


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

class setup(ThreeDScene):
    def construct(self):
        
        # Create a 3D cube
        rod = Cylinder(radius = 0.25, height = 8, direction=DOWN)
        brass1 = Sphere(radius = 0.75)
        brass2 = Sphere(radius = 0.75)
        brass1.next_to(rod, DOWN, buff=0)
        brass2.next_to(rod, UP, buff=0)
        
        # Set up the camera orientation
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)

        # Set the focal length to zoom out (higher focal length = zoom out)
        self.camera.focal_distance = 10

                
        self.play(Create(rod))
        self.wait(1)
        self.play(Create(brass1))
        self.wait(1)
        self.play(Create(brass2))
        # self.play(Rotate(rod, angle=PI/4, axis=UP))
        self.wait()

class deriveG(Scene):
    def construct(self):
        t1 = MathTex(r'\tau_{net} = 0 = F_gL \times -k\theta')
        t1.shift(UP * 3)
        self.play(Create(t1))

        self.wait(1)
        t2 = MathTex(r"F_g = \frac{k\theta}{L}")
        t2.next_to(t1, DOWN)
        self.play(Create(t2))

        self.wait(1)
        t3 = MathTex(r"F_g = \frac{GMm}{r^2}")
        t3.next_to(t2, DOWN)
        self.play(Create(t3))

        self.wait(1)
        t4 = MathTex(r"\frac{k\theta}{L} = \frac{GMm}{r^2}")
        t4.next_to(t3, DOWN)
        self.play(Create(t4))

        self.wait(1)
        t5 = MathTex(r"G = \frac{k\theta r^2}{LMm}")
        t5.next_to(t4, DOWN)
        self.play(Create(t5))

        self.wait(1)
        t6 = MathTex(r"G = \frac{\frac{m_{rod}L^2}{12}+2m(\frac{L}{2})^2(\frac{2\pi}{T})^2\theta r^2}{LMm}")
        t6.next_to(t5, DOWN)
        self.play(Create(t6))
        self.wait(2)

