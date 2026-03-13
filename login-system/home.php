<?php
session_start();

// cek login dan role
if (!isset($_SESSION['login']) || $_SESSION['role'] != 'user') {
    header("Location: index.php");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Home User</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Selamat datang, <?= $_SESSION['username']; ?>! 🎉</h2>

        <p>Yeay!!! Anda berhasil login sebagai <b>User</b>.</p>

        <a href="logout.php" class="logout-btn">Logout</a>
    </div>

</body>
</html>
