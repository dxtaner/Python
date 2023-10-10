import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını okuyarak verileri DataFrame'e yükleme
df = pd.read_excel('DailyActivities.xlsx')

# Kişilere göre verileri ayarlama
charles_data = df.loc[df['Area of Interest'] == 'Charles', df.columns[1:]]
henry_data = df.loc[df['Area of Interest'] == 'Henry', df.columns[1:]]
susan_data = df.loc[df['Area of Interest'] == 'Susan', df.columns[1:]]

# Aktivite alanlarını alarak grafik için x eksenini belirleme
activities = df['Area of Interest']

# Birleşik çubuk grafik oluşturma
width = 0.2
x = range(len(activities))
plt.bar(x, charles_data.values[0], width=width, label='Charles')
plt.bar([i + width for i in x], henry_data.values[0],
        width=width, label='Henry')
plt.bar([i + 2 * width for i in x],
        susan_data.values[0], width=width, label='Susan')

# Grafik özelleştirmeleri
plt.xlabel('Area of Interest')
plt.ylabel('Time Spent (hours)')
plt.title('Time Spent on Daily Activities per Person')
plt.xticks([i + width for i in x], activities, rotation=45)
plt.legend()

# Grafik gösterme veya kaydetme
plt.tight_layout()
plt.show()
