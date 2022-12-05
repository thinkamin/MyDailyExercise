from manimlib import *
class My(Scene):
    def construct(self):
        polygon1 = Rectangle()
        polygon1.set_fill(BLUE_E,1)
        self.play(ShowCreation(polygon1))
        self.wait()

        polygon2 = RoundedRectangle()
        polygon2.set_fill(BLUE_E,1)
        self.play(ShowCreation(polygon2))
        self.wait()

        polygon3 = Arc()
        polygon3.set_fill(BLUE_E,1)
        self.play(ShowCreation(polygon3))
        self.wait()

        polygon4 = Sector()
        polygon4.set_fill(BLUE_E,1)
        self.play(ShowCreation(polygon4))
        self.wait()

        '''
        polygon5 = Circle()
        polygon5.set_fill(BLUE_E,1)
        self.play(ShowCreation(polygon5))
        self.wait()

        '''
        polygon6 = Annulus()
        polygon6.set_fill(RED,1)
        self.play(ShowCreation(polygon6))
        self.wait()
        polygon7 = Dot()
        polygon7.set_fill(RED_E,1)
        self.play(ShowCreation(polygon7))
        self.wait()
        polygon8 = Ellipse()
        polygon8.set_fill(RED_E,1)
        self.play(ShowCreation(polygon8))
        self.wait()
        polygon9 = Arrow()
        polygon9.set_fill(RED_E,1)
        self.play(ShowCreation(polygon9))
        self.wait()
        polygon10 = ArrowTip()
        polygon10.set_fill(RED_E,1)
        self.play(ShowCreation(polygon10))
        self.wait()


        
        



