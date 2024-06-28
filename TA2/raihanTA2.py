# Import library yang diperlukan
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

# Load dataset dari file CSV
df = pd.read_csv('ai4i2020.csv')

# Pisahkan fitur (X) dan label (y)
# Drop kolom-kolom yang tidak digunakan sebagai fitur
X = df.drop(labels=['UDI', 'Product ID', 'Type', 'Air temperature [K]', 'Process temperature [K]', 
                    'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Machine failure'], axis=1)
y = df['Machine failure']  # Kolom 'Machine failure' sebagai target (label)

# Memisahkan dataset menjadi data latih (X_train, y_train) dan data uji (X_test, y_test)
# dengan rasio 80:20 menggunakan train_test_split. random_state=42 digunakan untuk hasil yang dapat direproduksi.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melakukan penskalaan fitur menggunakan StandardScaler
# agar setiap fitur memiliki mean 0 dan varians 1 untuk meningkatkan performa model.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Skala data yang dilatih
X_test = scaler.transform(X_test)        # Skala data yang diuji

# Memilih model klasifikasi RandomForestClassifier dengan parameter random_state=42 untuk hasil yang konsisten saat dilatih ulang.
model = RandomForestClassifier(random_state=42)

# Latih model dengan data latih
model.fit(X_train, y_train)

# Menggunakan model yang telah dilatih untuk memprediksi label dari data uji (X_test).
y_pred = model.predict(X_test)

# Evaluasi model dengan metrik precision
# Precision adalah metrik yang penting dalam kasus ini untuk mengukur seberapa banyak dari prediksi positif yang benar-benar positif.
# Precision tinggi menunjukkan bahwa model membuat sedikit kesalahan dalam memprediksi kelas positif.
precision = precision_score(y_test, y_pred)
print(f'Precision: {precision:.2f}')
