# Gunakan image dasar PHP dengan Apache
FROM php:8.2-apache

# Salin file PHP dan CSS ke dalam direktori kerja di kontainer
COPY index.php /var/www/html/
COPY style.css /var/www/html/
COPY flag.txt /
# Atur direktori kerja
WORKDIR /var/www/html

# Ubah izin file agar Apache dapat membacanya
RUN chown -R www-data:www-data /var/www/html

# Ekspose port 80 untuk web server
EXPOSE 80

# Mulai Apache
CMD ["apache2-foreground"]
