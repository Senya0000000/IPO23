import Nod_Nok
import area_of_quadrilateral
a = 25
b = 30
Nod_result = Nod_Nok.Nod(a, b)
Nok_result = Nod_Nok.Nok(a, b)
print("Наименьший общий делитель (", a, ",", b, ") =", Nod_result)
print("Наименьшее общее кратное (", a, ",", b, ") =", Nok_result)
side1 = 6
side2 = 9
side3 = 15
side4 = 8
diagonal = 17
area = area_of_quadrilateral.area_of_quadrilateral(side1, side2, side3, side4, diagonal)
print("Площадь четырехугольника =", area)