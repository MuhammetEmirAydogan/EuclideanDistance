# Matematiksel işlemleri yapmak için kullandığımız kütüphanemiz
import math

# Öklid mesafesi hesaplayan fonksiyonumuz
"""
    İki nokta arasındaki Öklid mesafesini hesaplar.
    parametre point1: Birinci nokta (x1, y1)
    parametre point2: İkinci nokta (x2, y2)
    return: Öklid mesafesi
"""
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D uzayda noktaları içeren listemiz
points = [(2, 3), (5, 7), (1, 1), (6, 5), (3, 4)]

# Mesafeleri saklamak için oluşturduğumuz boş bir liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplamak için kullandığımız döngüler
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulmak için
min_distance = min(distances)

# Sonuçları yazdırdık
print("Noktalar:", points)
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)
