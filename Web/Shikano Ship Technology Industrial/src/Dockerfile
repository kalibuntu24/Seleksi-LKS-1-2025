# Gunakan image dasar Python
FROM python:3.10-slim

# Atur direktori kerja di dalam kontainer
WORKDIR /app

# Salin file requirements dan instal dependensi
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Salin semua file aplikasi ke direktori kerja
COPY . .

# Ekspose port 5000 untuk aplikasi
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
