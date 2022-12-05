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
        to_isolate = ['B','C','=','(',')']
        lines = VGroup(
                Tex('A^2+B^2=C^2'),
                Tex('A^2=C^2-B^2'),
                Tex('A^2=(C+B)(C-B)',isolate=['A^2',*to_isolate]),
                Tex('A=\\sqrt{(C+B)(C-B)}',isolate=['A',*to_isolate])
                )
        lines.arrange(DOWN,buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                'A':BLUE,
                'B':TEAL,
                'C':GREEN,
                })

        self.add(lines[0])
        self.play(
                TransformMatchingTex(
                    lines[0].copy(),lines[1],
                    path_arc=90*DEGREES,
                ),run_time=2)
        self.wait()








if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
