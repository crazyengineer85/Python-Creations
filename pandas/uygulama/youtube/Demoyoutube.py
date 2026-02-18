import pandas as pd
# 1- İlk 10 kaydı getiriniz.
# print(df.head(10))
# 2- İkinci 5 kaydı getiriniz.
# df = df[6:11].head(5) # ilk önce slicingle satırı al sonra head 5 al
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
# x = df.columns # butun columns isim
# df = len(df.columns) # butu colon sayısı
# print(f"tüm kolonlar: {x}, \n\n total sayısı: {df}")
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1, inplace=True)
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
# 7- En çok görüntülenen video hangisidir ?
# 8- En düşük görüntülenen video hangisidir?
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# 12- Her kategoride kaç video vardır ?
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


df = pd.read_csv("GBvideos.csv")
# df = df["likes"].mean() 
# print(df)
result = df["dislikes"].mean()
print(result)







"""
🔥 Altın Kural

Kendine şu soruyu sor:

Bu işlem df’i kalıcı olarak değiştirmeli mi?

✅ Evet → df = df.method()

❌ Hayır → sadece df.method()

💡 Gerçek Hayat Örneği
Geçici filtre:
df[df["Age"] > 30]

Bu sadece gösterir.

Kalıcı filtre:
df = df[df["Age"] > 30]

Artık df’in içinde sadece 30 yaş üstü kalır.
"""




# df = (df.dropna().query("Age>25").sort_values("Salary", ascending=False))
