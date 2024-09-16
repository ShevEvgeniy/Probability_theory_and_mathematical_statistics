import math
import numpy as np
from numpy import linalg as LA
from scipy import stats
import statistics

# функция вычисляет статистику критеря для проверки гипотезы равенства
# средних двух парных выборок
# x, y - выборки одинакового объема
def equalmean(x,y):
    # вычисляем разность выборок
    dif=mothers-daughters
    n=len(dif)
    # вычисляем среднее разности
    mean_dif=dif.mean()
    # вычисляем несмещенную дисперсию разности
    var_dif=dif.var()*n/(n-1)
    # вычисляем t-статистику
    t=mean_dif/math.sqrt(var_dif)*math.sqrt(n)
    # вычисляем р-уровень
    p = 1 - math.fabs(stats.t.cdf(t,n-1) - stats.t.cdf(-t,n-1))
    return t,p
    

mothers=np.array([172,177,158,170,178,175,164,160,169,165])
daughters=np.array([173,175,162,174,175,168,155,170,160,163])
t,p=equalmean(mothers,daughters)
print("t-статистика критерия = ",t)
print("p-уровень = ",p)
alpha=float(input("Введите уровень значимости "))
if p>alpha:
    print("статистически значимых различий в росте матерей и дочерей нет")
else:
    print("есть статистически значимые различия в росте матерей и дочерей")
print("\n Проверка с помощью встроенной функции")
res=stats.ttest_rel (a=mothers, b=daughters)
print("t-статистика критерия = ",res.statistic)
print("p-уровень = ",res.pvalue)