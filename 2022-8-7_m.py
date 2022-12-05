from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-08-07

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
最终结果相关用红色
'''
class Test(Scene):
    def construct(self):
        #english_font = 'Times New Roman'
        chinese_font = 'Microsoft YaHei'
        #color_map = it.cycle(BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE)#next(color_map)
        def point2dot_tex(point,a,position=UP,color=WHITE):
            dot = Dot(point).set_fill(color)
            t = Tex(a).next_to(dot,position)
            self.play(ShowCreation(dot),Write(t))
        def draw_line(point1,point2):
            line = Line(point1,point2,color=RED)
            self.play(ShowCreation(line))
        def showstr(string,position=2.7*DOWN,font=chinese_font):
            text = Text(string,font=chinese_font).shift(position)
            self.play(FadeIn(text))
            self.wait(1)
            self.play(FadeOut(text))

        # grid = NumberPlane()
        # self.add(grid)
        text = Text("Here is a text",font='Consolas',font_size=90)
        difference = Text(
                """
                The most important difference between Text and Tex is that \n
                you can change the font more easily,but can't use the LaTeX grammar
                """,
                font='Arial',font_size=24,
                t2c={'Text':BLUE,'Tex':BLUE,"LaTex":ORANGE})
        VGroup(text,difference).arrange(DOWN,buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference,UP))
        self.wait(3)
        
        fonts = Text(
            "And you can also set the font according to different words",
            font="Arial",
            t2f={"font":'Consolas',"words":"Consolas"},
            t2c={'font':BLUE,'words':GREEN}
                )

        fonts.set_width(FRAME_WIDTH-1)
        slant = Text(
            "And the same as slant and weight",
            font='Consolas',
            t2s={'slant':ITALIC},
            t2w={'weight':BOLD},
            t2c={'slant':ORANGE,'weight':RED}
                )
        VGroup(fonts,slant).arrange(DOWN,buff=0.8)
        self.play(FadeOut(text),FadeOut(difference,shift=DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 



font
font_size
t2s
t2c
t2w

