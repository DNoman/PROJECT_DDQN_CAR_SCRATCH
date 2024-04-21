import pygame


class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.isactiv = False

    def draw(self, win):
        pygame.draw.line(win, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 2)


# the file of shame
def getGoals():
    goals = []

    goal1 = Goal(0, 200, 167, 203)
    goal2 = Goal(0, 100, 161, 186)
    goal2_5 = Goal(0, 0, 150, 130)
    goal3 = Goal(120, 0, 170, 120)
    goal3_5 = Goal(200, 0, 200, 120)
    goal4 = Goal(270, 0, 270, 110)
    goal4_5 = Goal(363 ,9,367, 91)
    goal5 = Goal(450, 0, 450, 137)
    goal5_5 = Goal(525, 0, 525, 142)  #
    goal6 = Goal(583, 7, 582, 141)
    goal6_5 = Goal(642, 10, 638, 142)
    goal7_5 = Goal(685, 57, 740, 131)########
    goal8 = Goal(754, 141, 794, 16)
    goal9 = Goal(754, 141, 881, 55)
    goal9_5 = Goal(755, 142, 909, 137)
    goal10 = Goal(754, 144, 887, 232)
    goal10_5 = Goal(755, 146, 771, 275)
    goal11 = Goal(716, 139, 720, 278)
    goal12 = Goal(674, 137, 685, 275)
    goal13 = Goal(636, 136, 634, 284)
    goal13_1 = Goal(615, 182, 581, 265)
    goal15 = Goal(554, 139, 558, 277)
    goal16 = Goal(526, 138, 513, 271)
    goal17 = Goal(482, 138, 474, 268)
    goal17_1 = Goal(430, 137, 415, 281)
    goal17_2 = Goal(369, 139, 380, 271)
    goal17_3 = Goal(341, 139, 362, 285)
    goal17_4 = Goal(269, 151, 362, 284)
    goal17_5 = Goal(163, 210, 361, 282)
    goal17_6 = Goal(144, 302, 362, 286)
    goal17_7 = Goal(201, 370, 357, 289)
    goal17_8 = Goal(303, 449, 390, 314)
    goal17_9 = Goal(381, 458, 431, 310)
    goal17_10 = Goal(427, 461, 482, 308)
    goal17_11 = Goal(477, 457, 535, 314)
    goal17_12 = Goal(534, 452, 592, 314)
    goal17_13 = Goal(589, 447, 643, 312)
    goal17_14 = Goal(641, 458, 686, 309)
    goal17_14_1 = Goal(718 ,345, 730 ,432)
    goal17_16 = Goal(728, 453, 843, 319)
    goal17_17 = Goal(761, 458, 916, 367)
    goal17_18 = Goal(761, 457, 969, 456)
    goal17_19 = Goal(764, 456, 963, 545)
    goal17_20 = Goal(766, 458, 865, 594)

    goal18 = Goal(750, 460, 750, 600)
    goal19 = Goal(670, 460, 670, 600)
    goal19_5 = Goal(590, 460, 590, 600)
    goal20 = Goal(510, 460, 510, 600)
    goal20_5 = Goal(430, 460, 430, 600)
    goal21 = Goal(350, 460, 350, 600)
    goal21_5 = Goal(280, 460, 278, 600)
    goal22 = Goal(190 ,490,233, 560)
    goal22_5_1 = Goal(171 ,486,171, 599)
    goal22_5 = Goal(80,600,175,440)
    goal23 = Goal(150,420,0,570)
    goal23_5 = Goal(0,450,130,400)
    goal24 = Goal(0,380,130,380)

    goals.append(goal1)
    goals.append(goal2)
    goals.append(goal2_5)
    goals.append(goal3)
    goals.append(goal3_5)
    goals.append(goal4)
    goals.append(goal4_5)
    goals.append(goal5)
    goals.append(goal5_5)
    goals.append(goal6)
    goals.append(goal6_5)
    goals.append(goal7_5)
    goals.append(goal8)
    goals.append(goal9)
    goals.append(goal9_5)
    goals.append(goal10)
    goals.append(goal10_5)
    goals.append(goal11)
    goals.append(goal12)
    goals.append(goal13)
    goals.append(goal13_1)
    goals.append(goal15)
    goals.append(goal16)
    goals.append(goal17)
    goals.append(goal17_1)
    goals.append(goal17_2)
    goals.append(goal17_3)
    goals.append(goal17_4)
    goals.append(goal17_5)
    goals.append(goal17_6)
    goals.append(goal17_7)
    goals.append(goal17_8)
    goals.append(goal17_9)
    goals.append(goal17_10)
    goals.append(goal17_11)
    goals.append(goal17_12)
    goals.append(goal17_13)
    goals.append(goal17_14)
    goals.append(goal17_14_1)
    goals.append(goal17_16)
    goals.append(goal17_17)
    goals.append(goal17_18)
    goals.append(goal17_19)
    goals.append(goal17_20)
    goals.append(goal18)
    goals.append(goal19)
    goals.append(goal19_5)
    goals.append(goal20)
    goals.append(goal20_5)
    goals.append(goal21)
    goals.append(goal21_5)
    goals.append(goal22)
    goals.append(goal22_5_1)
    goals.append(goal22_5)
    goals.append(goal23)
    goals.append(goal23_5)
    goals.append(goal24)

    goals[len(goals) - 1].isactiv = True

    return (goals)
