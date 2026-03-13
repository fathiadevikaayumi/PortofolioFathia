<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Edit</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-pink-100 p-6">
<h1 class="text-center text-2xl font-bold text-pink-700 mb-4">EDIT DATA</h1>

<?php
require 'koneksi.php';
$id = $_GET['id'];
$data = mysqli_query($conn, "SELECT * FROM gajidpr WHERE id='$id'");
$row = mysqli_fetch_array($data);
?>

<form action="editproses.php" method="POST" class="max-w-md mx-auto bg-white p-4 rounded shadow border border-pink-300 grid gap-3">
    <input type="hidden" name="id" value="<?= $row['id'] ?>">
    
    <input placeholder="Nama" class="p-2 border border-pink-300 rounded" name="nama" value="<?= $row['nama_anggota'] ?>">
    <input placeholder="Jabatan"class="p-2 border border-pink-300 rounded" name="jabatan" value="<?= $row['jabatan'] ?>">
    <input placeholder="Partai" class="p-2 border border-pink-300 rounded" name="partai" value="<?= $row['partai'] ?>">
    <input placeholder="Gaji" class="p-2 border border-pink-300 rounded" type="number" name="gaji" value="<?= $row['gaji_pokok'] ?>">
    <input placeholder="Tunjangan Rumah" class="p-2 border border-pink-300 rounded" type="number" name="rumah" value="<?= $row['tunjangan_rumah'] ?>">
    <input placeholder="Tunjangan Jabatan" class="p-2 border border-pink-300 rounded" type="number" name="tjabatan" value="<?= $row['tunjangan_jabatan'] ?>">
    <input placeholder="Tunjangan Transport" class="p-2 border border-pink-300 rounded" type="number" name="transport" value="<?= $row['tunjangan_transport'] ?>">

    <button class="bg-pink-600 text-white py-2 rounded hover:bg-pink-700">UPDATE</button>
</form>

</body>
</html>
