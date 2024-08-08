# Gunakan image Node.js resmi sebagai base image
FROM node:20

# Buat direktori kerja di dalam container
WORKDIR /usr/src/app

# Salin package.json dan package-lock.json ke dalam direktori kerja
COPY package*.json ./

# Install dependensi aplikasi
RUN npm install

# Salin seluruh kode aplikasi ke dalam direktori kerja
COPY app.js .
COPY index.html .
COPY page1.html .
COPY page2.html .
COPY flag.txt /

# Tentukan port yang akan diekspos
EXPOSE 3000

# Jalankan aplikasi
CMD ["node", "app.js"]
