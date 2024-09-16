import math
import numpy as np
from numpy import linalg as LA
from scipy import stats 
import statistics

# функция вычисляет доверительный интервал  для разности
# средних двух парных выборок
# x, y - выборки одинакового объема
#  gamma - доверительная вероятность
def interval_mean(x,y, gamma):
    # вычисляем разность выборок
    dif=x-y
    n=len(dif)
    # вычисляем среднее разности
    mean_dif=dif.mean()
    # вычисляем несмещенную дисперсию разности
    var_dif=dif.var()*n/(n-1)
    # вычисляем стандартное отклонение
    s=math.sqrt(var_dif)
    # вычисляем квантиль распределения Стьюдента
    tkvant=stats.t.ppf((1 + gamma)/2, n-1)
    # вычисляем левую границу
    left=mean_dif-tkvant*s/math.sqrt(n)
    # вычисляем правую границу
    right=mean_dif+tkvant*s/math.sqrt(n)
    return left,right
    

mothers=np.array([178,165,165,173,168,155,160,164,178,175])
daughters=np.array([175,167,154,174,178,148,160,167,169,170])
a,b=interval_mean(mothers,daughters,0.95)
print("95% доверительный интервал для разности средних матерей и дочерей:")
print("(",a," ; ",b,")")
print("\n Проверка с помощью встроенной функции")
dif=mothers-daughters
rez=stats.t.interval(confidence=0.95, df=len(dif)-1, loc=dif.mean(), scale=stats.sem(dif))
print(rez)