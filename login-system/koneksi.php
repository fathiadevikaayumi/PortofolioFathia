<?php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "login_db1";

$koneksi = mysqli_connect($host, $user, $pass, $db);

if (!$koneksi) {
    die("Koneksi database gagal");
}
