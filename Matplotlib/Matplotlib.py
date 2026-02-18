import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [1,4,9,16,25]


# plt.plot(x,y)
# plt.axis([0,8,0,64]) # grafik çizgisi düzlem içinde küçülür
# plt.axis([0,4,0,20]) # grafik çizgisi düzlemden taşar




# plt.plot(x,y,color ="red", linewidth="5") # renk ve çizgi kalınlığı belirlenir
# plt.plot(x,y,":g") # ":" çizginin nokta nokta çizilmesi
# plt.plot(x,y,"o--g") # "o" grafik çizgisine kırılma nboktasına belirleme
# plt.plot(x,y,"o-.b", linewidth= 8)
# plt.plot(x, y,
#          marker="o",
#          linestyle="-.",
#          markerfacecolor="yellow",
#          markeredgecolor="red",
#          color="blue",
#          linewidth=8)
"""

Açıklama kısa kısa:

color="blue" → çizgi rengi

markerfacecolor="red" → marker içi

markeredgecolor="red" → marker kenarı

marker="o" → yuvarlak nokta

linestyle="-." → kesik-noktalı çizgi

linewidth=8 → kalınlık (string değil, integer olmalı)
"""
# plt.title("Sayısal Veri Grafiği") # Başlık ekleme
# plt.xlabel("yatay düzlem")
# plt.ylabel("dikey düzlem")
# renk eklemede: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html buradan kontrol et
# plt.show()


# x = np.linspace(0,5,100)
# plt.plot(x, label="linear")
# plt.plot(x**2, label="quadratic")
# plt.plot(x**3, label="cubic")

# # plt.xlabel("yatay düzlem")
# # plt.ylabel("dikey düzlem")
# # plt.legend()
# # plt.legend(loc="upper right")
# plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
# plt.title("veri analizi",
#           fontsize=20,
#           fontweight="bold",
#           fontfamily="serif",
#           color="purple")
# plt.xlabel("yatay düzlem",
#           fontsize=20,
#           fontweight="bold",
#           fontfamily="serif",
#           color="purple")
# plt.ylabel("dikey düzlem",
#           fontsize=20,
#           fontweight="bold",
#           fontfamily="serif",
#           color="purple")
# plt.gca().set_facecolor("lightgray") # grafik arka plan içi rengi
# plt.gcf().set_facecolor("lightblue") # tüm sayfa arka plan içi rengi
# plt.xticks(fontsize=14, fontweight="bold", rotation=45, color = "red", fontstyle="italic")
# plt.yticks(fontsize=14, fontweight="bold")
# plt.show()




"""


plt.legend(loc=1)   # 1 = upper right

"upper left"

"lower right"

"lower left"

"center"

"best" (otomatik en uygun yer)

Tamam cankuş, grafiğin dışına alıyoruz 😎

Legend’i sağ tarafa, grafiğin dışına almak için `bbox_to_anchor` kullanıyoruz:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,100)

plt.plot(x, label="linear")
plt.plot(x**2, label="quadratic")
plt.plot(x**3, label="cubic")

plt.xlabel("yatay düzlem")
plt.ylabel("dikey düzlem")

plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
```

### Mantık:

* `loc="upper left"` → legend’in kendi referans noktası
* `bbox_to_anchor=(1,1)` → grafiğin sağ üst dış köşesi
* `tight_layout()` → kesilme olmasın diye

İstersen tam ortaya sağ dışa da alabiliriz:

```python
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
```

Şimdi grafik biraz profesyonel sunum havasına girdi 👌


"""



# aynı düzlem(sayfa) birkaç grafik gösterme
x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)
# plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
# plt.legend(loc=4)
axs[0].plot(x,x, color="red")
axs[0].set_title("linear")
axs[1].plot(x,x**2, color="green")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3)
axs[2].set_title("cubic")

plt.tight_layout()
plt.show()








# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2)


# axs[0,0].plot(x,x, color="red", label="linear")
# axs[0,0].set_title("linear")
# axs[0,0].legend()
# axs[0,1].plot(x,x**2, color="green", label="quadratic")
# axs[0,1].set_title("quadratic")
# axs[0,1].legend()
# axs[1,0].plot(x,x**3, color="blue", label="cubic")
# axs[1,0].set_title("cubic")
# axs[1,0].legend()
# axs[1,1].plot(x,x**4, color="yellow", label="4. üssü")
# axs[1,1].set_title("4. üssü")
# axs[1,1].legend()
# fig.suptitle("sayı")
# fig.supxlabel("yatay düzlem")
# fig.supylabel("dikey düzlem")



# plt.legend(loc=.....) 1- sağ üst 2- sol üst 3- sol alt 4- sağ alt






# fig.legend(loc="upper left")


import pandas as pd

# df = pd.read_csv("nba.csv")
# df = df.drop(["Number"],axis=1).groupby("Team").mean(numeric_only=True) # mean() "numeric_only=True" yazmazsan TypeError: dtype 'str' does not support operation 'mean' hatası alırsın 
# df.plot(subplots=True, legend=True)
# # plt.legend()
# plt.gcf().suptitle("nba",
#           fontsize=20,
#           fontweight="bold",
#           fontfamily="serif",
#           color="purple")
# plt.xticks(fontsize=10, fontweight="bold", rotation=15, color = "red")
# # plt.gca().set_facecolor("lightgray") # grafik arka plan içi rengi
# # plt.gcf().set_facecolor("lightblue") # tüm sayfa arka plan içi rengi

# plt.show()




