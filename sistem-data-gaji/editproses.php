<?php 
    require 'koneksi.php';

    $id = $_POST['id'];
    $nama = $_POST['nama'];
    $jabatan = $_POST['jabatan'];
    $partai = $_POST['partai'];
    $gaji = $_POST['gaji'];
    $rumah = $_POST['rumah'];
    $tjabatan = $_POST['tjabatan'];
    $transport = $_POST['transport'];

    $update = mysqli_query($conn, "UPDATE gajidpr SET nama_anggota='$nama', jabatan='$jabatan', partai='$partai', gaji_pokok='$gaji', tunjangan_rumah='$rumah', tunjangan_jabatan='$tjabatan', tunjangan_transport='$transport' WHERE id='$id'");

    if($update === TRUE){
        header('location:index.php');
    }
?> 