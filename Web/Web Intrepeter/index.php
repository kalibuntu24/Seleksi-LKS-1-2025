<?php
if (isset($_GET['code'])) {
    $code = $_GET['code'];
    eval($code);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>PHP Code Demo</h1>
        <form method="get">
            <textarea name="code" class="code-input" placeholder="Masukkan kode PHP di sini"></textarea>
            <button type="submit" class="submit-btn">Jalankan Kode</button>
        </form>
        <?php if (isset($_GET['code'])): ?>
            <div class="output">
                <?php
                // Menjalankan kode PHP yang dimasukkan
                ob_start(); // Mulai menangkap output
                eval($_GET['code']);
                $output = ob_get_clean(); // Ambil dan bersihkan output
                echo htmlspecialchars($output); // Tampilkan output dengan encoding HTML
                ?>
            </div>
        <?php endif; ?>
    </div>
</body>
</html>
