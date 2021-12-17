import time
import math

#e = math.exp(1.0)
#height = radius * math.sin(radians)

def area(radius):
    a=math.pi*radius**2
    return a

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    #print("result is:", result)
    return result

distance(1,2,4,6)

def hypotenuse(x, y):
    cateta1 = x**2
    cateta2 = y**2
    ipotenuza_la_patrat = cateta1 + cateta2
    ipotenuza = math.sqrt(ipotenuza_la_patrat)
    print(ipotenuza)
    return 0.0

#hypotenuse(3, 4)

#radius = distance(xc, yc, xp, yp)

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    print(result)
    return result

#circle_area(1,2, 4, 6)

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
is_divisible(9, 4)

print("12"*3)
s5 = 'Yanjun Xu, fost vicedirector al Diviziei a VI-a a Biroului din ' \
     'Jiangsu al Ministerului Securităţii Statului (MSS), principala ' \
     'agenţie de informaţii a Partidului Comunist Chinez (PCC), a fost ' \
     'găsit vinovat recent în SUA de „conspiraţie şi tentativă de spionaj ' \
     'economic şi furt de secrete comerciale”. Acest proces a fost posibil' \
     ' în urma unei operaţiuni de contraspionaj, prin intermediul căreia ' \
     'Yanjun Xu a fost atras în afara Chinei, arestat şi adus în SUA pentru' \
     ' a fi judecat în baza unor indicii că a încercat să fure o tehnologie avansată. ' \
     'Acest caz nu este decât ultimul dintr-o serie de operaţiuni ' \
     'de spionaj duse de Beijing pentru a fura secrete militare şi ' \
     'industriale din SUA şi de la partenerii lor, chiar şi din Rusia, ' \
     'o metodă care a permis armatei chineze să-şi facă rapid un arsenal ' \
     'de arme sofisticate.'

print(len(s5)-3)


s6 = 'Maria este medic.'
print('ar' not in s6)

n = int(input('n='))
s = 0
while n!=0:
    n = n // 10
    s = s + 1
print(s)

