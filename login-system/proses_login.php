<?php
session_start();
include "koneksi.php";

$username = $_POST['username'];
$password = $_POST['password'];

$query = mysqli_query($koneksi, "SELECT * FROM users WHERE username='$username'");
$data  = mysqli_fetch_assoc($query);

if ($data) {
    if (password_verify($password, $data['password'])) {

        // buat session
        $_SESSION['login']    = true;
        $_SESSION['username'] = $data['username'];
        $_SESSION['role']     = $data['role'];

        // arahkan sesuai role
        if ($data['role'] == 'admin') {
            header("Location: admin.php");
        } else {
            header("Location: home.php");
        }
        exit;

    } else {
        echo "
        <p>Password salah.</p>
        <a href='index.php'>Kembali ke Login</a>
        ";
    }
} else {
    echo "
    <p>Username belum terdaftar.</p>
    <a href='registrasi.php'>Daftar akun di sini</a><br><br>
    <a href='index.php'>Kembali ke menu Login</a>
    ";
}
?>
