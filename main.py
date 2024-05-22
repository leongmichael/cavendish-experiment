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
        
        rod = Cylinder(radius = 0.15, height = 8, direction=DOWN)
        rod.set_fill(color=GOLD)

        brass1 = Sphere(radius = 0.5)
        brass2 = Sphere(radius = 0.5)
        brass1.set_fill(color=GOLD)
        brass2.set_fill(color=GOLD)
        brass1.next_to(rod, DOWN, buff=0)
        brass2.next_to(rod, UP, buff=0)

        rope = Cylinder(radius = 0.05, height = 8, direction=RIGHT)
        rope.set_fill(color=GRAY)
        rope.next_to(rod, RIGHT, buff=0)


        group = VGroup(rod, brass1, brass2, rope)

        angle = PI/12

        line = Line(start=10 * DOWN, end=10 * UP, stroke_width=0.3) # 0 
        line2 = Line(start=10 * DOWN, end=10 * UP, stroke_width=0.3) # 1
        line2.rotate(angle + 8 * DEGREES, about_point=ORIGIN)
        line3 = Line(start=10 * DOWN, end=10 * UP, stroke_width=0.3) # 2
        line3.rotate(-(angle + 8 * DEGREES), about_point=ORIGIN)
        
        # Set up the camera orientation
        # phi is up, theta is left/right
        self.set_camera_orientation(phi=120 * DEGREES, theta=0 * DEGREES)

        # Set the focal length to zoom out (higher focal length = zoom out)
        self.camera.focal_distance = 10

                
        self.play(Create(group), Create(line), Create(line2), Create(line3))
        self.play(Rotate(group, angle=angle, axis=RIGHT, about_point=group.get_center()), run_time=2)
        self.play(Rotate(group, angle=-2 * angle, axis=RIGHT, about_point=group.get_center()), run_time=2)
        self.play(Rotate(group, angle=2 * angle, axis=RIGHT, about_point=group.get_center()), run_time=2)
        self.play(Rotate(group, angle=-2 * angle, axis=RIGHT, about_point=group.get_center()), run_time=2)



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
        self.play(Create(t0, run_time=3))
        self.wait(1)
        temp1 = MathTex(r'2(F_g\frac{L}{2})')
        temp_copy = temp1.copy().move_to(t0[2].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy))
        self.wait(1)
        temp1 = MathTex(r'F_gL')
        temp_copy = temp1.copy().move_to(t0[2].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy))
        self.wait(1)
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

        #create the "zero" expression for fading in effect
        zero = MathTex(r'0')
        zero.move_to(UP * 2.85 + LEFT * 2.2) #manual movement into proper place

        self.play(t0.animate.shift(UP*2.8)) #animate shift
        self.play(FadeOut(t0[0]))
        self.play(FadeIn(zero))
        self.wait(1)

        #Line 2 transform Fg = Ktheta/L
        path =  ArcBetweenPoints(temp_copy.get_center(), zero.get_center()+LEFT*0.5, angle=PI/2, stroke_width=8) #create arcpath, parameters: (start, stop, arc path)
        self.play(FadeOut(temp_copy[0]), run_time=0.3)
        temp_copy.remove(temp_copy[0])
        self.play(MoveAlongPath(temp_copy, path), FadeOut(zero), run_time=1) #animate movement along path
        
        #clean equation t0 to reflect new equation
        t0.remove(t01)
        self.play(t0.animate.shift(RIGHT * 1.4)) #shift equation to the center of the screen

        #line 3, 4 combined (merge 2 equations into one effect)
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

        #line 5, answer expression
        self.wait(1)
        t6 = MathTex(r"G \;=\; \frac{(\frac{m_{rod}(L)^2}{12}+2m(\frac{L}{2})^2)(\frac{2\pi}{T})^2\theta r^2}{LMm}")
        t6.next_to(t5, DOWN*2)
        t6.shift(RIGHT*1.2) # shift this to the center of the screen
        #t6.move_to(t6.get_center()+LEFT*2)
        self.play(Create(t6, run_time=4))
        self.wait(1)

        #create box around answer
        box = SurroundingRectangle(t6, color=BLUE, buff=0.3, corner_radius=0.1)

        #draw box
        self.add(box, t6)
        self.play(Create(box))
        self.wait(3)


class deriveGWithK(Scene):
    def construct(self):

        #Line 1 0 = FgL - ktheta
        t01 = MathTex(r'\tau_{net}')
        t02 = MathTex(r'=')
        t03 = MathTex(r'\tau_{gravity}')
        t041 = MathTex(r'+')
        t042 = MathTex(r'\tau_{wire}')
        t04 = VGroup(t041, t042).arrange(RIGHT, buff =0.5)
        t0 = VGroup(t01, t02, t03, t04).arrange(RIGHT, buff = 0.2)
        self.play(Create(t0, run_time=3))
        self.wait(10) 
        temp1 = MathTex(r'2(F_g\frac{L}{2})')
        temp_copy = temp1.copy().move_to(t0[2].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy))
        self.wait(11)
        temp1 = MathTex(r'F_gL')
        temp_copy = temp1.copy().move_to(t0[2].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy))
        self.wait(1)
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

        #create the "zero" expression for fading in effect
        zero = MathTex(r'0')
        zero.move_to(UP * 2.85 + LEFT * 2.2) #manual movement into proper place

        self.play(t0.animate.shift(UP*2.8)) #animate shift
        self.play(FadeOut(t0[0]))
        self.play(FadeIn(zero))
        self.wait(10)

        #Line 2 transform Fg = Ktheta/L
        path =  ArcBetweenPoints(temp_copy.get_center(), zero.get_center()+LEFT*0.5, angle=PI/2, stroke_width=8) #create arcpath, parameters: (start, stop, arc path)
        self.play(FadeOut(temp_copy[0]), run_time=0.3)
        temp_copy.remove(temp_copy[0])
        self.play(MoveAlongPath(temp_copy, path), FadeOut(zero), run_time=1) #animate movement along path
        
        #clean equation t0 to reflect new equation
        t0.remove(t01)
        self.play(t0.animate.shift(RIGHT * 1.4)) #shift equation to the center of the screen

        #line 3, 4 combined (merge 2 equations into one effect)
        t2 = MathTex(r" \frac{k\theta}{L}")
        t3 = MathTex(r"\frac{GMm}{r^2}")
        r_transform = VGroup(t2, MathTex("="), MathTex(r"F_g"), MathTex("="), t3)
        r_transform.arrange(direction=RIGHT, buff=1)
        r_transform.next_to(t0, DOWN*1.2)
        r_transform.move_to(r_transform.get_center()+RIGHT*1.85)
        self.play(Create(r_transform[:3]))
        self.wait(1)
        self.play(Create(r_transform[3:]))
        self.wait(11)

        # The mobs replace each other and none are left behind
        self.play(FadeOut(r_transform[2]), FadeOut(r_transform[3]))
        self.play(r_transform[4].animate.shift(LEFT*3))
        r_transform.remove(r_transform[2])
        r_transform.remove(r_transform[3])

        self.wait(1)
        t5 = MathTex(r"\frac{k\theta r^2}{LMm} \;=\; G")
        t5.next_to(r_transform, DOWN*1.5)
        t5.move_to(t5.get_center()+LEFT*1.1)
        self.play(Create(t5))

        #create box around answer
        box = SurroundingRectangle(t5, color=BLUE, buff=0.3, corner_radius=0.1)

        #draw box
        self.add(box, t5)
        self.play(Create(box))
        self.wait(10)

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

class rotationalIntertiaK(Scene):
    def construct(self):
        #animate first line k <- torsion constant
        k = Text("k")
        text = Text("<- torsion constant")
        text.move_to(RIGHT)
        self.play(Create(k))
        self.wait(0.5)
        self.play(k.animate.shift(LEFT*2.5))
        self.play(FadeIn(text, shift=RIGHT))
        self.wait(2)
        self.play(FadeOut(k), FadeOut(text))

        #create inertia equation
        t01 = MathTex(r'I_{net}')
        t02 = MathTex(r'=')
        t03 = MathTex(r'I_{point\,mass}')
        t04 = MathTex(r'+')
        t05 = MathTex(r'I_{point\,mass}')
        t06 = MathTex(r'+')
        t07 = MathTex(r'I_{rotating\,rod}')
        t0 = VGroup(t01, t02, t03, t04, t05, t06, t07).arrange(RIGHT, buff = 0.2)
        self.play(Create(t0)) #animate original equation
        self.wait(0.5)
        #animate replacement #1
        temp1 = MathTex(r'm(\frac{L}{2})^2')
        temp_copy1 = temp1.copy().move_to(t0[2].get_center())
        temp_copy2 = temp1.copy().move_to(t0[4].get_center())
        self.play(ReplacementTransform(t0[2], temp_copy1), ReplacementTransform(t0[4], temp_copy2))
        self.wait(1)
        #animate replacement #2
        temp1 = MathTex(r'\frac{m_{rod}(L)^2}{12}')
        temp_copy3 = temp1.copy().move_to(t0[6].get_center())
        self.play(ReplacementTransform(t0[6], temp_copy3))
        self.wait(1)
        
        #combine 
        t3 = MathTex(r"\frac{GMm}{r^2}")
        r_transform = VGroup(t01, t02, temp_copy1, t04, temp_copy2, t06, temp_copy3)
        temp4 = MathTex(r'2m(\frac{L}{2})^2')
        temp_copy4 = temp4.copy().move_to(r_transform[4].get_center()+LEFT*1.3)

        self.play(
            FadeOut(r_transform[2], run_time=0.3), FadeOut(r_transform[3], run_time=0.3),
            r_transform[0].animate.shift(RIGHT*1.4),
            r_transform[1].animate.shift(RIGHT*1.5),
            r_transform[4].animate.shift(LEFT*1.3), ReplacementTransform(r_transform[4], temp_copy4),
            r_transform[5].animate.shift(LEFT*1.3),
            r_transform[6].animate.shift(LEFT)
            )
        self.wait(1)
        r_transform.remove(temp_copy1)
        r_transform.remove(t04)
        r_transform.remove(temp_copy2)
        r_transform.add(temp_copy4)
        self.play(r_transform.animate.shift(UP*3))
        self.wait(1)

        #animate Inet
        t2 = MathTex(r'k = I_{net} (\frac{2\pi}{T})^2')
        t2.next_to(r_transform, DOWN*2)
        self.play(Create(t2))
        self.wait(1)

        #animate k equation
        t3 = MathTex(r'\therefore k = (\frac{m_{rod}(L)^2}{12} + 2m(\frac{L}{2})^2)\;(\frac{2\pi}{T})^2')
        t3.next_to(t2, DOWN*2)
        self.play(Create(t3, run_time = 2))
        self.wait(2)

        box = SurroundingRectangle(t3, color=BLUE, buff=0.3, corner_radius=0.1)

        #draw box
        self.add(box, t3)
        self.play(Create(box))
        self.wait(1)

class intro(Scene):
    def construct(self):
        #create line
        start_point = (-2, 0, 0)  # Adjust coordinates as needed
        end_point = (2, 0, 0)
        line = Line(start_point, end_point)
        arrow_size = 8  # Adjust for desired arrow size
        arrow = Arrow(
            end_point - RIGHT * arrow_size / 2,  # Shift starting point left
            end_point,
            buff=0,  # No separation between arrow and line
        )
        self.play(Create(arrow, run_time=2.5))

        F = Text("F", font_size=400)
        F.next_to(arrow, DOWN)
        self.play(Create(F), arrow.animate.shift(UP*3), F.animate.shift(UP*3))
        self.wait(1)

        vectorF = VGroup(F, arrow)
        self.play(ScaleInPlace(vectorF, 0.15, run_time=1))
        self.play(vectorF.animate.shift(UP*1.5))
        self.wait(1)
        law2 = Text("Newton's Second Law of Motion", font_size=45)
        law2.next_to(vectorF, RIGHT)
        law2.move_to(UP*3.5)
        t0 = MathTex(' = ma', font_size=70)
        self.play(vectorF.animate.shift(LEFT))
        t0.next_to(vectorF, RIGHT)
        self.play(Create(law2), FadeIn(t0, shift=RIGHT))
        self.wait(1)

        secondLaw = VGroup(vectorF, t0, law2)

        law1 = Text('Newton\'s First Law (for Rotation)', font_size=45)
        law1.move_to(law2.get_center()+DOWN*2.5)
        t1 = Tex('An object at rest remains at rest, or if in motion, remains in motion at a constant velocity unless acted on by a net external force.', font_size = 35)
        t1.next_to(law1, DOWN)
        self.play(Create(law1))
        self.play(Create(t1))
        self.wait(1)

        law3 = Text('Newton\'s Law of Universal Gravitation', font_size=40)
        law3.move_to(law1.get_center()+DOWN*2.5)
        t2 = MathTex(r'F_G = G\frac{m_1m_2}{r^2}')
        t2.next_to(law3, DOWN*1.5)
        self.play(Create(law3))
        self.play(Create(t2))
        
        self.wait(15)

class gravitation(Scene):
    def construct(self):
        #create 2 base newton law equations
        t01 = MathTex(r'F =')
        t02 = MathTex(r'ma')
        t0 = VGroup(t01, t02).arrange(RIGHT)
        t0t = Text("Newton's First Law", font_size=30)
        t0.move_to(UP*2.5+LEFT*3)
        t0t.next_to(t0, UP*2.3)
        t11 = MathTex(r'F_g') 
        t12 = MathTex(r'= \frac{Gmm}{r^2}') 
        t1 = VGroup(t11, t12).arrange(RIGHT)
        t1t = Text("Newton's Law of Gravitation", font_size=30)
        t1.move_to(UP*2.5+RIGHT*3)
        t1t.next_to(t1, UP)
        
        #fade out text
        self.play(Create(t0), Create(t0t))
        self.play(Create(t1), Create(t1t))
        self.wait(1)
        self.play(FadeOut(t0t), FadeOut(t1t))

        self.wait(1)
        
        #line merge
        r_transform = VGroup(t01, t02, t11, t12)
        self.wait(0.5)
        #animate replacement #1
        temp1 = MathTex(r"= \frac{GM_{Earth}m}{r_{Earth}^2}")
        temp_copy1 = temp1.copy().move_to(r_transform[3].get_center())
        self.play(ReplacementTransform(r_transform[3], temp_copy1), t11.animate.shift(LEFT*0.6))
        r_transform.add(temp_copy1)
        r_transform.remove(t12)
        self.wait(10)

        # animate f = ma -> f = mg
        temp2 = MathTex(r"mg")
        temp_copy2 = temp2.copy().move_to(r_transform[1].get_center())
        self.play(ReplacementTransform(r_transform[1], temp_copy2))
        r_transform.add(temp_copy2)
        r_transform.remove(t02)
        self.wait(10)


        # TODO: find better wya to animmate this. the current method of shifting the text by the index numebr is not ideal because the indexes get shifted as well from the method above
        # The mobs replace each other and none are left behind
        self.play(FadeOut(r_transform[0]), FadeOut(r_transform[1]))
        self.play(r_transform[3].animate.shift(RIGHT*1.5), r_transform[2].animate.shift(LEFT*2.2))
        r_transform.remove(r_transform[0])
        r_transform.remove(r_transform[2])

        self.wait(1)

        t2 = MathTex(r"r_{Earth}^2g= GM_{Earth}")
        t2.next_to(r_transform, DOWN)
        t2.move_to(UP*0.3)
        self.play(Create(t2))
        self.wait(1)
        box = SurroundingRectangle(t2, color=BLUE, buff=0.3, corner_radius=0.1)
        #draw box
        self.add(box, t2)
        self.play(Create(box))
        self.wait(10)

        t3 = MathTex(r'\text{Where,}\: r_{Earth} = 61378.1\: \text{kilometers}')
        t3.next_to(t2, DOWN)
        t3.move_to(DOWN)
        t4 = MathTex(r'g=9.8m/s^2')
        t4.next_to(t3, DOWN)
        t4.move_to(DOWN*1.7+RIGHT*0.3)
        self.play(Create(t3))
        self.wait(12)
        self.play(Create(t4))
        
        self.wait(30)
        
        
class deriveKFromT(Scene):
    def construct(self):
        periodT = MathTex(r'T')
        periodRest = MathTex(r'= 2\pi \sqrt{\frac{I_{net}}{k}}')
        periodT.next_to(periodRest, LEFT)
        self.play(Create(periodT), Create(periodRest))
        self.wait(15)

        periodTSquared = MathTex(r'T^2')
        periodRestSquared = MathTex(r'= (2\pi)^2 \frac{I_{net}}{k}')
        periodTSquared.next_to(periodRestSquared, LEFT)
        self.play(ReplacementTransform(periodRest, periodRestSquared), ReplacementTransform(periodT, periodTSquared))
        self.wait(1)

        # Multiplying both sides by k
        periodTSquaredK = MathTex(r'k T^2')
        periodRestSquaredK = MathTex(r'= (2\pi)^2 I_{net}')
        periodTSquaredK.next_to(periodRestSquaredK, LEFT)
        self.play(ReplacementTransform(periodRestSquared, periodRestSquaredK), ReplacementTransform(periodTSquared, periodTSquaredK))
        self.wait(1)

        # Dividing both sides by T^2
        k0 = MathTex(r'k')
        kRest0 = MathTex(r'= \frac{(2\pi)^2 I_{net}}{T^2}')
        k0.next_to(kRest0, LEFT)
        self.play(ReplacementTransform(periodTSquaredK, k0), ReplacementTransform(periodRestSquaredK, kRest0))
        self.wait(1)


        k = MathTex(r'k')
        kRest = MathTex(r'=  (\frac{2\pi}{T})^2I_{net}')
        k.next_to(kRest, LEFT)
        self.play(ReplacementTransform(k0, k), ReplacementTransform(kRest0, kRest))

        group = VGroup(k, kRest)

        #create box around answer
        box = SurroundingRectangle(group, color=BLUE, buff=0.3, corner_radius=0.1)

        #draw box
        self.add(box, group)
        self.play(Create(box))
        self.wait(20)

class cavendishExperimentText(Scene):
    def construct(self):
        cavendishExperiment = Text("Cavendish Experiment", font_size=45)
        cavendishExperiment.move_to(UP*3)
        self.play(Create(cavendishExperiment))
        self.wait(30)

class hookesLaw(Scene):
    def construct(self):
        hookeslaw = MathTex(r'\tau = -k\theta')
        self.play(Create(hookeslaw))
        self.wait(10)






        


