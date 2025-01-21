# Gerekli kütüphanelerin import edilmesi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

# Eğitim verisinin yüklenmesi ve özelliklerin ölçeklenmesi
dataset_train = pd.read_csv('input/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Özelliklerin ölçeklenmesi
scaler = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = scaler.fit_transform(training_set)

# 60 zaman adımı ve 1 çıktı içeren veri yapısının oluşturulması
X_train, y_train = [], []
for i in range(60, len(training_set_scaled)):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

# Verilerin yeniden şekillendirilmesi
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# RNN modelinin oluşturulması
model = Sequential()

# İlk LSTM katmanının ve Dropout düzenlemesinin eklenmesi
model.add(LSTM(units=50, return_sequences=True,
          input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))

# İkinci LSTM katmanının ve Dropout düzenlemesinin eklenmesi
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

# Üçüncü LSTM katmanının ve Dropout düzenlemesinin eklenmesi
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

# Dördüncü LSTM katmanının ve Dropout düzenlemesinin eklenmesi
model.add(LSTM(units=50))
model.add(Dropout(0.2))

# Çıktı katmanının eklenmesi
model.add(Dense(units=1))

# Modelin derlenmesi
model.compile(optimizer='adam', loss='mean_squared_error')

# Modelin eğitim verisi ile eğitilmesi
model.fit(X_train, y_train, epochs=100, batch_size=32)

# Tahminlerin yapılması ve sonuçların görselleştirilmesi
# 2017'nin gerçek hisse senedi fiyatlarının alınması
dataset_test = pd.read_csv('input/Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# 2017'nin tahmin edilen hisse senedi fiyatlarının alınması
dataset_total = pd.concat(
    (dataset_train['Open'], dataset_test['Open']), axis=0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60, len(inputs)):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_stock_price = model.predict(X_test)
predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

# Sonuçların görselleştirilmesi
plt.plot(real_stock_price, color='red',
         label='Gerçek Google Hisse Senedi Fiyatı')
plt.plot(predicted_stock_price, color='blue',
         label='Tahmin Edilen Google Hisse Senedi Fiyatı')
plt.title('Google Hisse Senedi Fiyatı Tahmini')
plt.xlabel('Zaman')
plt.ylabel('Google Hisse Senedi Fiyatı')
plt.legend()
plt.show()
