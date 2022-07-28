from doctest import DocTestSuite
#from termios import CWERASE
from manim import *

class Linear_Reg(Scene):

    def construct(self):
        #Introduction - Topic
        screen = FullScreenRectangle()
        title=Text('Linear Regression',t2c={'[:1]':'#3174f0', '[1:2]': '#e53125',
                                            '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                                            '[4:5]': '#269a43', '[5:6]': '#e53125',
                                            '[7:8]':'#3174f0', '[8:9]': '#e53125',
                                            '[9:10]': '#fbb003', '[10:11]': '#3174f0',
                                            '[12:14]': '#269a43', '[14:15]': '#e53125',
                                            '[15:]':'#3174f0'}, font_size=35).scale(2)
        subtitle=Tex("By Tanushree B S and Elizabeth Mary Mathew",font_size=25)
        subcorner=Tex("- Using Least Square Method",color="#936d52",font_size=20)

        title.shift(0.5*UP)
        subtitle.next_to(title,DOWN)
        subcorner.shift(DR)
        self.add_sound("LR-intro.mp3")
        self.play(Write(title),Write(subtitle),Write(subcorner))
        self.wait(9)
        self.play(ApplyMethod(title.shift, 3*UP))
        self.play(FadeOut(title,subtitle,subcorner))

        #Explanation of Linear Regression
        ax1 = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"color":GREEN},
            tips=False
        ).add_coordinates()
        axis_labels=ax1.get_axis_labels(Tex("No. Of Hours Studied").scale(0.7), Text("Scores in Exams").scale(0.45))
        point1 = Dot(ax1.coords_to_point(2, 15), radius=0.12, color="#93526c")
        point2 = Dot(ax1.coords_to_point(3, 30), radius=0.12, color="#93526c")
        point3 = Dot(ax1.coords_to_point(4, 60), radius=0.12, color="#93526c")
        point4 = Dot(ax1.coords_to_point(6, 60), radius=0.12, color="#93526c")
        point5 = Dot(ax1.coords_to_point(7, 75), radius=0.12, color="#93526c")
        point6 = Dot(ax1.coords_to_point(8, 60), radius=0.12, color="#93526c")
        eqn = Tex("Y=m(x)+c",color="YELLOW",font_size=55)
        eqn.shift(LEFT*4)
        txt1 = Text("Where : \ny = Depenendent Variable\nx = Independent Variable\nm = Slope or Gradient (how steep the line is)\nc = the Y Intercept \n(where the line crosses the Y axis)",color="YELLOW",font_size=18)
        txt1.shift(RIGHT*5)
        self.add_sound("def_LR.mp3")
        self.play(Create(ax1))
        self.play(Write(axis_labels))
        self.add(point1,point2,point3,point4,point5,point6)
        curve1 = ax1.plot(lambda x: (9.10)*x + 6.166, x_range=[0,10,1], color="RED")
       
        self.play(Create(curve1))
        self.wait(8)
        self.add_sound("slope eqn.mp3")
        self.play(Write(eqn))
        self.play(Write(txt1))
        self.wait(9)
        self.remove(ax1,axis_labels,point1,point2,point3,point4,point5,point6,curve1,eqn,txt1)
        
        # plotting of points and non linear functions
        self.add_sound("datapoints.mp3")
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 12, 1],
            tips=False
        ).add_coordinates()

        t2 = MathTable(
            [["x", 2, 4, 6, 8],
             ["y", 3, 7, 5, 10]],
        )

        self.play(Create(t2))
        self.wait(1)

        self.play(ScaleInPlace(t2, 0.4))
        t2.generate_target()
        t3 = t2.target.move_to(3*UP)
        self.play(MoveToTarget(t2))

        y_label = ax.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = ax.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)
        graphs = VGroup()

        self.play(Create(ax))
        self.play(Create(grid_labels))

        # set of points
        pts = ((2, 3),
               (4, 7),
               (6, 5),
               (8, 10))
        dot_1 = Dot(ax.coords_to_point(2, 3), radius=0.06)
        dot_2 = Dot(ax.coords_to_point(4, 7), radius=0.06)
        dot_3 = Dot(ax.coords_to_point(6, 5), radius=0.06)
        dot_4 = Dot(ax.coords_to_point(8, 10), radius=0.06)
        dots = VGroup(dot_1, dot_2, dot_3, dot_4)

        for j in range(0, 4):
            c1 = t2.get_entries((1, j+2))
            c2 = t2.get_entries((2, j+2))
            dot1 = Dot(ax.coords_to_point(
                *pts[j]), radius=0.06, color="#00FFFF")
            dot1l = VGroup(dot1, Text(
                str(pts[j]), font_size=20).next_to(dot1, UP))
            self.play(FadeToColor(c1, "#00FFFF"),
                      FadeToColor(c2, "#00FFFF"), Create(dot1l))
            self.play(FadeToColor(c1, "#FFFFFF"),
                      FadeToColor(c2, "#FFFFFF"))
        self.wait(2)

        self.add_sound("goal_pred.mp3")
        # creating non linear connections - 1
        p1 = Line(ax.coords_to_point(
            *pts[0]), ax.coords_to_point(*pts[1]), color="#00FFFF")
        p1.points[1:3] += UP*2
        self.wait(2)
        self.play(Create(p1))
        p2 = Line(ax.coords_to_point(
            *pts[1]), ax.coords_to_point(*pts[2]), color="#00FFFF")
        p2.points[1:3] += DOWN
        self.play(Create(p2))
        p3 = Line(ax.coords_to_point(
            *pts[2]), ax.coords_to_point(*pts[3]), color="#00FFFF")
        p3.points[1] += UP+RIGHT
        p3.points[2] += DOWN
        self.play(Create(p3))
        self.wait(7)
        curve1 = VGroup(p1, p2, p3)
        self.wait(4)

        # Adding a new ctest point (3,7.95)
        self.add_sound("new_data_point1.mp3")
        t2n = MathTable(
            [["x", 2, 4, 6, 8, 3],
             ["y", 3, 7, 5, 10, 7.95]],
        ).scale(0.4)

        t2n.move_to(3*UP)
        self.play(Transform(t2, t2n))
        c1 = t2n.get_entries((1, 6))
        c2 = t2n.get_entries((2, 6))
        dotn1 = Dot(ax.coords_to_point(3, 7.95), radius=0.13, color="#F9E076")
        dotn1l = VGroup(dotn1, Text(
            "(3,7.95)", font_size=20).next_to(dotn1, UP))
        self.play(FadeToColor(c1, "#00FFFF"),
                  FadeToColor(c2, "#00FFFF"), Create(dotn1l))
        self.wait(5)
        self.play(FadeToColor(c1, "#FFFFFF"),
                  FadeToColor(c2, "#FFFFFF"))
        self.wait(4)

        # creating non linear connections - 2
        pd1 = Line(ax.coords_to_point(
            *pts[0]), ax.coords_to_point(*pts[1]), color="#00FFFF")
        pd1.points[1:3] += DOWN*2
        # self.play(Create(pd1))
        pd2 = Line(ax.coords_to_point(
            *pts[1]), ax.coords_to_point(*pts[2]), color="#00FFFF")
        pd2.points[1] += UP*2
        pd2.points[2] += DOWN*2
        # self.play(Create(pd2))
        pd3 = Line(ax.coords_to_point(
            *pts[2]), ax.coords_to_point(*pts[3]), color="#00FFFF")
        pd3.points[1] += UP*1.5
        # self.play(Create(pd3))
        self.wait(2)
        curve2 = VGroup(pd1, pd2, pd3)
        self.wait(7)
        self.play(FadeOut(dotn1l), FadeOut(c2), FadeOut(c1))
        self.play(Transform(curve1, curve2))
        self.wait(2)
       
        # Adding a new ctest point (3,1.95) 
        self.add_sound("new_data_point2.mp3")
        t2n = MathTable(
            [["x", 2, 4, 6, 8, 3],
             ["y", 3, 7, 5, 10, 1.95]],
        ).scale(0.4)

        t2n.move_to(3*UP)
        self.play(Transform(t2, t2n))
        c1 = t2n.get_entries((1, 6))
        c2 = t2n.get_entries((2, 6))
        dotn1 = Dot(ax.coords_to_point(3, 1.95), radius=0.13, color="#F9E076")
        dotn1l = VGroup(dotn1, Text(
            "(3, 1.95)", font_size=20).next_to(dotn1, DOWN+0.1*RIGHT))
        self.play(FadeToColor(c1, "#00FFFF"),
                  FadeToColor(c2, "#00FFFF"), Create(dotn1l))
        self.wait(1)
        self.play(FadeToColor(c1, "#FFFFFF"),
                  FadeToColor(c2, "#FFFFFF"))

        self.play(FadeOut(curve1), FadeOut(dotn1l), FadeOut(c1), FadeOut(c2))
        self.wait(8)

        ##
        self.add_sound("linearfuncn.mp3")
        t3 = MathTable(
            [["x", 2, 4, 6, 8],
             ["y", 3, 7, 5, 10]],
        ).scale(0.4)

        t3.move_to(3*UP)
        self.play(ReplacementTransform(t2, t3))

        # changing the colour of the vertices
        self.play(FadeToColor(dots, "#ECAD8F"))

        # drawing a line1 - connecting two points
        line_graph_1 = ax.plot(lambda x: 0.5*x+2, color="#ECAD8F")

        self.play(Create(line_graph_1))
        self.wait(2)

        # drawing a line2- connecting two points
        line_graph_2 = ax.plot(lambda x: -1*x+11, color="#ECAD8F")
        self.play(Transform(line_graph_1, line_graph_2))
        self.wait(2)

        # drawing a line3- connecting two points
        line_graph_2 = ax.plot(lambda x: 1.1666*x+0.666, color="#ECAD8F")
        self.play(Transform(line_graph_1, line_graph_2))
        self.wait(2)

        # changing the colour of the vertices
        self.play(FadeToColor(dots, "#Fe78c9"), FadeOut(line_graph_1))
        self.wait(2)

        self.add_sound("lsm def.mp3")

        lsq=Text("LSM - Used to determine the \nline of best fit for set of data",font_size=15,color=RED)
        lsq.shift(RIGHT*4)
        self.play(Write(lsq))
        mse_eqn=Text("MSE = summation of squared\n(difference between \noriginal & predicted value",font_size=15,color=RED)
        mse_eqn.shift(LEFT*4)
        self.play(Write(mse_eqn))
        self.wait(8)
        self.remove(lsq,mse_eqn)

        # calculating error for each of the above random lines - 1 - MSE = 21.250
        self.add_sound("1st graph mse.mp3")
        line_graph_1 = ax.plot(lambda x: -1*x+11, color="#Fe78c9")
        self.play(Create(line_graph_1))
        self.wait()

        l1_dl1 = DashedLine(ax.coords_to_point(2, 3), ax.coords_to_point(
            2, 9), color="#Fe78c9", stroke_width=3)
        l1_dl2 = DashedLine(ax.coords_to_point(8, 10), ax.coords_to_point(
            8, 3), color="#Fe78c9", stroke_width=3)
        self.play(Create(l1_dl1), Create(l1_dl2))

        self.wait(6)

        self.add_sound("2nd graph.mp3")
        mse2 = Text("MSE = 36 + 49 / 4", color="#77DD77", font_size=23)
        mse_res2 = Text("= 21.250", color="RED", font_size=29)
        self.play(t3.animate.shift(LEFT*2))
        mse2.next_to(t3, RIGHT*1.5)
        mse_res2.next_to(mse2, RIGHT)
        self.play(Write(mse2))
        self.play(Write(mse_res2))
        self.wait(2)
        self.play(FadeToColor(dots, "#77DD77"), FadeOut(line_graph_1), FadeOut(
            l1_dl1), FadeOut(l1_dl2), FadeOut(mse2), FadeOut(mse_res2), t3.animate.shift(RIGHT*2))

        # calculating error for each of the above random lines - 2 - MSE=6.250

        line_graph_1 = ax.plot(lambda x: 0.5*x+2, color="#77DD77")
        self.play(Create(line_graph_1))
        self.wait()

        l1_dl1 = DashedLine(ax.coords_to_point(4, 7), ax.coords_to_point(
            4, 4), color="#77DD77", stroke_width=3)
        l1_dl2 = DashedLine(ax.coords_to_point(8, 10), ax.coords_to_point(
            8, 6), color="#77DD77", stroke_width=3)
        self.play(Create(l1_dl1), Create(l1_dl2))

        mse = Text("MSE = 9 + 16 / 4", color="#77DD77", font_size=23)
        mse_res = Text("= 6.250", color="RED", font_size=29)
        self.play(t3.animate.shift(LEFT*2))
        mse.next_to(t3, RIGHT*1.5)
        mse_res.next_to(mse, RIGHT)
        self.play(Write(mse))
        self.play(Write(mse_res))

        self.wait(2)
        self.play(FadeToColor(dots, "#F9e076"), FadeOut(line_graph_1), FadeOut(
            l1_dl1), FadeOut(l1_dl2), FadeOut(mse), FadeOut(mse_res), t3.animate.shift(RIGHT*2))
        self.wait(2)

        # calculating error for each of the above random lines - 3 - MSE = 3.275
        self.add_sound("3rd graph.mp3")
        line_graph_1 = ax.plot(lambda x: 1.1666*x+0.666, color="#F9e076")
        self.play(Create(line_graph_1))
        self.wait()

        l1_dl1 = DashedLine(ax.coords_to_point(4, 7), ax.coords_to_point(
            4, 5.33), color="#F9e076", stroke_width=3)
        l1_dl2 = DashedLine(ax.coords_to_point(6, 5), ax.coords_to_point(
            6, 7.665), color="#F9e076", stroke_width=3)
        self.play(Create(l1_dl1), Create(l1_dl2))

        mse3 = Text("MAE = 6 + 7.1022 / 4", color="#77DD77", font_size=23)
        mse_res3 = Text("= 3.275", color="RED", font_size=29)
        self.play(t3.animate.shift(LEFT*2))
        mse3.next_to(t3, RIGHT*1.5)
        mse_res3.next_to(mse3, RIGHT)
        self.play(Write(mse3))
        self.play(Write(mse_res3))
        self.play(t3.animate.shift(RIGHT*2),FadeOut(mse3),FadeOut(mse_res3),FadeOut(line_graph_1),FadeToColor(dots, "#bb86fc"),FadeOut(l1_dl1),FadeOut(l1_dl2))
        self.wait(5)

        # calculating the final random regression line with least error - MSE = 3.233
        self.add_sound("4th graph.mp3")
        line_graph_1 = ax.plot(lambda x: 0.95*x+0.47, color="#bb86fc")
        self.play(Create(line_graph_1))
        self.wait()

        l1_dl1 = DashedLine(ax.coords_to_point(2, 3), ax.coords_to_point(
            2, 2.37), color="#bb86fc", stroke_width=3)
        l1_dl2 = DashedLine(ax.coords_to_point(4, 7), ax.coords_to_point(
            4, 4.27), color="#bb86fc", stroke_width=3)
        l1_dl3 = DashedLine(ax.coords_to_point(6, 5), ax.coords_to_point(
            6, 6.17), color="#bb86fc", stroke_width=3)
        l1_dl4 = DashedLine(ax.coords_to_point(8, 10), ax.coords_to_point(
            8, 8.07), color="#bb86fc", stroke_width=3)
        self.play(Create(l1_dl1), Create(l1_dl2),Create(l1_dl3),Create(l1_dl4))
        mse3 = Text("MSE = 0.396 + 7.452 + 1.36 + 3.724 / 4", color="#77DD77", font_size=23)
        mse_res3 = Text("= 3.233", color="RED", font_size=29)
        self.play(t3.animate.shift(LEFT*2.4))
        mse3.next_to(t3, RIGHT*1.5)
        mse_res3.next_to(mse3, RIGHT)
        self.play(Write(mse3))
        self.play(Write(mse_res3))
        self.play(t3.animate.shift(RIGHT*2.4),FadeOut(mse3),FadeOut(mse_res3))
        self.wait(6)

        ####

        self.add(screen, graphs, grid_labels, dot1l,
                t2, c1, p1, p2, p3, pd1, pd2, pd3)

        
