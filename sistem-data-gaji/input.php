<?php
    require 'koneksi.php';

    $nama = $_POST['nama'];
    $jabatan = $_POST['jabatan'];
    $partai = $_POST['partai'];
    $gaji = $_POST['gaji'];
    $rumah = $_POST['rumah'];
    $tjabatan = $_POST['tjabatan'];
    $transport = $_POST['transport'];

    $create = mysqli_query($conn, "INSERT INTO gajidpr VALUES(NULL, '$nama', '$jabatan', '$partai', '$gaji', '$rumah', '$tjabatan', '$transport')");

    if($create === TRUE){
        header("location:index.php");
    }
?>