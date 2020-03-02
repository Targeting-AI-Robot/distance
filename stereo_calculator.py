import math

B = 0.139
seta_0 = 62.2
x_0 = 1280

def deg2rad(deg):
	return 180*deg/math.pi

l_x = int(input())
r_x = int(input())
#s = 0.11225525948717949
s = -0.12160986444444445
D = (B*x_0)/(2*s*(l_x-r_x))

#D = (B*x_0)/(2*(math.tan(deg2rad(seta_0/2)))*(l_x-r_x))
#D = (B*x_0)/(2*(math.tan(seta_0/2 + s))*(l_x-r_x))

#S = (B*x_0)/(2*(480/39.3701)*(l_x-r_x))

print("distance m",D)
print("distance inch",D*39.3701)
#print(S)
