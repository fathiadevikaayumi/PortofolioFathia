<?php
session_start();

if (!isset($_SESSION['login']) || $_SESSION['role'] != 'admin') {
    header("Location: index.php");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Admin</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Selamat Datang</h2>
        <p>Halo Admin, <?= $_SESSION['username']; ?> 👑</p>

        <a href="logout.php" class="logout-btn">Logout</a>
    </div>
</body>
</html>
