import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f=pd.read_csv("curs.csv")

f["Дата"] = pd.to_datetime(f["Дата"], format="%d.%m.%Y")

plt.plot (f["Дата"], f["Офіційний курс гривні, грн"], color='green' , label = 'Зміни Алжирських динар')

plt.title("Курс Алжирськьх Динар")
plt.grid(True)
plt.legend(loc="upper left")
plt.gcf().autofmt_xdate()
plt.show()
