import manim
from manim import *

config.media_width = "100%"
config.verbosity = "WARNING"

#This code is to create 3 reference dots that give an idea of the scale of the UP, DOWN, RIGHT, LEFT units
"""
origin = Dot()

        # Reference points along positive axes
        x_axis_point = Dot(RIGHT)
        y_axis_point = Dot(UP)

        # Group and position the points
        reference_points = VGroup(origin, x_axis_point, y_axis_point)
        reference_points.arrange(RIGHT, buff=0.5)

        self.add(reference_points)
        """

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

        #Line 1 0 = FgL - ktheta
        t01 = MathTex(r'\tau_{net}')
        t02 = MathTex(r'=')
        t03 = MathTex(r'\tau_{gravity}')
        t041 = MathTex(r'+')
        t042 = MathTex(r'\tau_{wire}')
        t04 = VGroup(t041, t042).arrange(RIGHT, buff =0.5)
        t0 = VGroup(t01, t02, t03, t04).arrange(RIGHT, buff = 0.2)
        self.play(Create(t0))
        self.wait(0.5)
        temp1 = MathTex(r'F_gL')
        temp_copy = temp1.copy().move_to(t0[2].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy))
        self.wait(0.5)
        t041n = MathTex(r'-')
        t042n = MathTex(r'k\theta')
        temp2 = VGroup(t041n, t042n).arrange(RIGHT, buff=0.5)
        # Create a temporary copy with the same position (idk why this works)
        temp_copy = temp2.copy().move_to(t0[3].get_center())
        # Perform replacement and remove the copy
        self.play(ReplacementTransform(t0[3], temp_copy),)
        t0.add(temp_copy)
        self.wait(1)
        self.play(FadeOut(t0, run_time=0.01))

        #tau = MathTex(r'\tau_{net}')
        #tau2 = MathTex(r' = F_gL - k\theta')
        zero = MathTex(r'0')
        zero.move_to(UP * 2.85 + LEFT * 2.2)

        self.play(t0.animate.shift(UP*2.8))
        self.play(FadeOut(t0[0]))
        self.play(FadeIn(zero))
        self.wait(1)

        #Line 2 transform Fg = Ktheta/L
        path =  ArcBetweenPoints(temp_copy.get_center(), zero.get_center()+LEFT*0.5, angle=PI/2, stroke_width=8)
        #temp_copy.remove(t041n)
        #self.play(FadeOut(t041n), run_time=0.5)
        #self.remove(t041n)
        self.play(FadeOut(temp_copy[0]), run_time=0.3)
        temp_copy.remove(temp_copy[0])
        self.play(MoveAlongPath(temp_copy, path), FadeOut(zero), run_time=1)
        
        #clean equation t0 to reflect new equation
        t0.remove(t01)
        self.play(t0.animate.shift(ORIGIN))

        #line 2, 3, 4
        t2 = MathTex(r" \frac{k\theta}{L}")
        t3 = MathTex(r"\frac{GMm}{r^2}")
        r_transform = VGroup(t2, MathTex("="), MathTex(r"F_g"), MathTex("="), t3)
        r_transform.arrange(direction=RIGHT, buff=1)
        r_transform.next_to(t0, DOWN*1.2)
        r_transform.move_to(r_transform.get_center()+RIGHT*1.85)
        self.play(Create(r_transform[:3]))
        self.wait(1)
        self.play(Create(r_transform[3:]))
        self.wait(1)

        # The mobs replace each other and none are left behind
        self.play(FadeOut(r_transform[2]), FadeOut(r_transform[3]))
        self.play(r_transform[4].animate.shift(LEFT*3))
        r_transform.remove(r_transform[2])
        r_transform.remove(r_transform[3])

        self.wait(1)
        t5 = MathTex(r"\frac{k\theta r^2}{LMm} \;=\; G")
        t5.next_to(r_transform, DOWN*1.4)
        t5.move_to(t5.get_center()+LEFT*1.1)
        self.play(Create(t5))

        self.wait(1)
        t6 = MathTex(r"\frac{(\frac{m_{rod}(L)^2}{12}+2m(\frac{L}{2})^2)(\frac{2\pi}{T})^2\theta r^2}{LMm} \;=\; G")
        t6.next_to(t5, DOWN*2)
        #t6.move_to(t6.get_center()+LEFT*2)
        self.play(Create(t6, run_time=4))
        self.wait(1)

        #box answer
        box = SurroundingRectangle(t6, color=BLUE, buff=0.3, corner_radius=0.1)

        # Add both the equation and the box to the scene
        self.add(box, t6)
        self.play(Create(box))
        self.wait(3)

class testArc(Scene):

    def construct(self):

        # Create text objects
        a = Text("a")
        equals1 = Text("=")
        b = Text("b")
        plus = Text("+")
        c = Text("c")
        minus = Text("-")

        # Arrange initial equation
        equation1 = VGroup(a, equals1, b, plus, c).arrange(RIGHT, buff=0.5)
        equation1.shift(UP * 2)

        # Animate writing of initial equation
        self.play(Write(equation1))
        self.wait(1)

        #move a left
        self.play(a.animate.shift(LEFT))
        
        #self.play(c.animate.shift(a.get_right() + RIGHT))
        path =  ArcBetweenPoints(c.get_center(), a.get_center() + RIGHT * 1, angle=PI/2, stroke_width=8)
        self.play(MoveAlongPath(c, path), FadeOut(plus), run_time=1)
        
        #you have to move the object before fading it in. the FadeIn method only makes the object appear at its position, but its position is already predetermined
        minus.move_to((a.get_center() + c.get_center())/2)
        self.play(FadeIn(minus))
        equation1.add(minus)
        equation1.remove(plus)

        #equation1.move_to(ORIGIN + UP*2)
        self.play(equation1.animate.shift(RIGHT + UP))
        self.wait(1)

class testCombine(Scene):
    def construct(self):
        r_transform = VGroup(Text("a "), Text("="), Text("b"), Text("="), Text("c"))

        r_transform.arrange(direction=RIGHT, buff=1)
        self.play(Create(r_transform))


        # The mobs replace each other and none are left behind
        self.play(FadeOut(r_transform[2]), FadeOut(r_transform[3]))
        self.play(r_transform[4].animate.shift(LEFT*3))
        r_transform.remove(r_transform[2])
        r_transform.remove(r_transform[3])
        t4 = MathTex(r"\frac{k\theta}{L} = \frac{GMm}{r^2}")
        t4.next_to(r_transform, DOWN)
        self.play(Create(t4))

        
