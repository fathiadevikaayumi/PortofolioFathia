<?php
include "koneksi.php";

$username = $_POST['username'];
$password = $_POST['password'];
$role     = $_POST['role']; // ambil role dari form

// cek username
$cek = mysqli_query($koneksi, "SELECT * FROM users WHERE username='$username'");
if (mysqli_num_rows($cek) > 0) {
    echo "Username sudah terdaftar. <a href='registrasi.php'>Kembali</a>";
    exit;
}

// hash password
$password_hash = password_hash($password, PASSWORD_DEFAULT);

// simpan ke database (termasuk role)
$query = mysqli_query(
    $koneksi,
    "INSERT INTO users (username, password, role)
     VALUES ('$username', '$password_hash', '$role')"
);

if ($query) {
    header("Location: index.php");
    exit;
} else {
    echo "Registrasi gagal";
}
?>
