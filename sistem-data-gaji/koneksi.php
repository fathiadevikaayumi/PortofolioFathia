<?php
    $conn = new mysqli('localhost', 'root', '', 'uprak11');

    if($conn->connect_error){
        die("Koneksi database gagal : ". $conn->connect_error);
    }
?>