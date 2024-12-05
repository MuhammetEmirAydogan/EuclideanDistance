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
