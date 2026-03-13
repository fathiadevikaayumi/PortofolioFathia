<?php
    require 'koneksi.php';
    
    $id=$_GET['id'];
    $delete = mysqli_query($conn, "DELETE FROM gajidpr WHERE id='$id'");

    if($delete === TRUE){
        header("location:index.php");
    }
?>