import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Title
st.title("Bike Sharing Data Analysis Dashboard")

#Subheader
st.subheader("Nama          : Muhammad Fadhlan Nafis")
st.subheader("Email         : muhammadfadhlannafis@gmail.com")
st.subheader("ID Dicoding   : mfadhlan_nafis")

#DataSet dari Github
data_day = pd.read_csv("https://raw.githubusercontent.com/mfadhlannafis/Belajar_Analisis_Data_Dengan_Python/main/day.csv")
data_hour = pd.read_csv("https://raw.githubusercontent.com/mfadhlannafis/Belajar_Analisis_Data_Dengan_Python/main/hour.csv")

#Menampilkan dataset
st.text("Data Set Penyewaan Sepeda Per Hari")
st.dataframe(data_day)

st.text("Data Set Penyewaan Sepeda Per Jam")
st.dataframe(data_hour)

#Penjelasan
#1.
st.subheader("Performa jumlah penyewaan sepeda per hari berdasarkan musim (season)")
# Menghitung total rental per musim
data_tren_season = data_day.groupby(by='season').agg({
    'cnt': 'sum',
    'casual': 'sum',
    'registered': 'sum'
})
# Membuat plot
fig, ax = plt.subplots()
data_tren_season.plot(kind='bar', ax=ax)
plt.xlabel("Season")
plt.ylabel("Total Rental (Millions)")
plt.title("Total Rental Bike per Season")
plt.xticks(rotation=45)
st.pyplot(fig)

#2.
st.subheader("Melihat modus berapa jam penyewaan sepeda")
# Menghitung modus per jam
data_mode_hour = data_hour.groupby(by='hr').agg({
    'cnt': 'max',
    'casual': 'max',
    'registered': 'max'
})
# Membuat plot
fig, ax = plt.subplots()
data_mode_hour.plot(kind='bar', ax=ax)
plt.xlabel("Hour")
plt.ylabel("Total Rental")
plt.title("Total Rental Bike per Hour")
st.pyplot(fig)

#3.
st.subheader("Jumlah penyewaan sepeda perhari berdasarkan musim 1 karena performanya penyewaan sepedanya kurang baik")
# Filter data untuk musim 1
data_filtered = data_day[data_day["season"] == 1]
# Menghitung total penyewaan per hari dalam musim 1
data_day_season1 = data_filtered.groupby(by='weekday').agg({
    'cnt': 'sum',
    'casual': 'sum',
    'registered': 'sum'
})
# Membuat plot
fig, ax = plt.subplots()
data_day_season1.plot(kind='line', ax=ax)
plt.xlabel("Day")
plt.ylabel("Total Rental")
plt.title("Total Rental Bike per Day in Season 1")
plt.xticks(rotation=45)
st.pyplot(fig)

#4.
st.subheader("Pengaruh temperatur terhadap jumlah penyewaan sepeda per hari")
# Membuat scatter plot dan regresi plot
plt.figure(figsize=(10, 5))
plt.scatter(data_day["cnt"], data_day["temp"])
plt.xlabel("Total Rental Bike per Day")
plt.ylabel("Temperature (°C)")
plt.title("Correlation Total Rental Bike per Day and Temperature")
sns.regplot(x=data_day["cnt"], y=data_day["temp"])
st.pyplot(plt)

#5.
st.subheader("Tren penyewaan sepeda dari 2011-2012 berdasarkan hari")
# Menghitung total penyewaan sepeda per hari dari 2011-2012
data_totalbike_per_day = data_day.groupby(by='yr').agg({
    'cnt': 'sum',
    'casual': 'sum',
    'registered': 'sum'
})
# Menampilkan data total penyewaan sepeda per hari dari 2011-2012
st.write("Total Rental Bike per Day (2011-2012):")
st.write(data_totalbike_per_day)
# Membuat plot
plt.plot(data_day["cnt"])
plt.xlabel("Day (2011-2012)")
plt.ylabel("Total Rental Bike")
plt.title("Total Rental Bike per Day (2011-2012)")
plt.xlim(0, len(data_day) - 1)  # Menyesuaikan batas sumbu x dengan jumlah data
plt.show()
st.pyplot(plt)

st.subheader("Kesimpulan")
st.text("1. Musim 3 memiliki performa bagus dalam total penyewaan sepeda per hari, sedangkan musim 1 memiliki performa buruk dalam total penyewaan sepeda per hari sehingga perlu dilakukan strategi yang tepat dalam meningkatkan minat pelanggan")
st.text("2. 18 dan 17 jam menjadi modus lama sewa penyewaan sepeda")
st.text("3. Strategi untuk meningkatkan minat pelanggan pada musim 1 dapat dibagi menjadi 2 strategi berbeda antara pelanggan registered dan pelanggan casual")
st.text("4. Hubungan temperatur dan total penyewaan sepeda per hari bersifat linear dan cukup kuat")
st.text("5. Total penyewaan sepeda 2012 lebih baik daripada 2011, tetapi pada akhir tahun 2012 total penyewaan sepeda mengalami penurunan, sehingga harus ada strategi khusus di awal tahun 2013")