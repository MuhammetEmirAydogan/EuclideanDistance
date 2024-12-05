# EuclideanDistance
# Öklid Mesafesi Hesaplayıcı

Bu proje, 2 boyutlu bir uzayda noktalar arasındaki Öklid mesafesini hesaplar. Python kullanarak mesafeleri hesaplama, sonuçları saklama ve minimum mesafeyi bulma işlemlerini gösterir.

## Özellikler

- Noktalar arasındaki Öklid mesafesini hesaplar.
- 2 boyutlu uzayda tanımlı bir listeyle çalışır.
- Tüm çiftler arasındaki en kısa mesafeyi bulur ve ekrana yazdırır.

## Nasıl Çalışır?

1. 2 boyutlu uzaydaki noktaların bir listesini tanımlayın.
2. Her benzersiz nokta çifti için mesafeyi hesaplayın.
3. `euclideanDistance` fonksiyonunu kullanarak mesafeyi hesaplayın.
4. Tüm mesafeleri bir listeye kaydedin ve en küçük olanı bulun.

## Kod Açıklaması

- **`euclideanDistance` Fonksiyonu**:  
  İki nokta `(x1, y1)` ve `(x2, y2)` arasındaki Öklid mesafesini hesaplar:
  ```python
  def euclideanDistance(point1, point2):
      return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

  points = [(2, 3),(5, 7),(1, 1),(6, 5),(3, 4)]

  for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
  
Noktalar: [(2, 3), (5, 7), (1, 1), (6, 5), (3, 4)]

Hesaplanan mesafeler: [5.0, 2.23606797749979, 4.47213595499958, 1.4142135623730951, 5.385164807134504, 3.605551275463989, 5.0, 4.123105625617661, 2.23606797749979, 3.605551275463989]
Minimum mesafe: 1.4142135623730951


