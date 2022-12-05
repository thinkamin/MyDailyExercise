from manimlib import *

class Mycoor(Scene):
    def construct(self):
        grid = NumberPlane((-10,10),(-5,5))

        self.play(ShowCreation(grid))
        self.wait()
        self.play(FadeOut(grid))

        grid2 = ComplexPlane((-10,10),(-5,5))
        self.play(ShowCreation(grid2))
        self.wait()
        self.play(FadeOut(grid2))

        # grid3 = CoordinateSystem((-10,10),(-5,5))
        # self.play(ShowCreation(grid3))
        # self.wait()
        # self.play(FadeOut(grid3))
        axes = Axes(
                x_range=(-1,10),
                y_range=(-2,2,0.5),
                height=6,
                width=10,
                axis_config={
                    "stroke_color":GREY_A,
                    "stroke_width":2,
                    },
                y_axis_config={
                    "include_tip":False,
                    })
                    
        axes.add_coordinate_labels(font_size=20,num_decimal_places=1,)
        self.add(axes)
    
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0,0))
        self.play(FadeIn(dot,scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3,2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5,0.5)))
        self.wait()
