import math
import sys

rx = 3280        #resolution for X
ry = 2464        #resolution for Y
#cx = rx//2		#principal point for X
#cy = ry//2		#principal point for Y
cx = 1659
cy = 1260
f = 2.803
h = 1066.4
#h = 809.8
vx = int(input())
vy = int(input())
x = int(input())
y = int(input())
#vx,vy = map(int,input().split()) #sosil_point
#x,y = map(int,input().split())  #object

tilt_ang = math.atan2(vy-cy,f)

u = (x-cx)/f
v = (y-cy)/f

C_P_ = h*math.tan(90+tilt_ang-math.atan(v))
CP_ = math.sqrt(h*h+(C_P_*C_P_))
Cp_ = math.sqrt(1+v*v)
PP_ = u*CP_/Cp_
d = math.sqrt((C_P_)*(C_P_)+(PP_*PP_))
print("distance mm",d)
print("distance inch",d/25.4) 
