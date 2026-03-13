<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-pink-100 p-6">
    <h1 class="text-2xl font-bold text-center mb-6 text-pink-700">
        PENDATAAN GAJI ANGGOTA DPR
    </h1>

    <!-- FORM INPUT -->
    <form action="input.php" method="POST" 
          class="max-w-md mx-auto bg-white p-4 rounded shadow border border-pink-300 grid gap-3">
        <input type="text" name="nama" placeholder="Nama" class="p-2 border border-pink-300 rounded">
        <input type="text" name="jabatan" placeholder="Jabatan" class="p-2 border border-pink-300 rounded">
        <input type="text" name="partai" placeholder="Nama Partai" class="p-2 border border-pink-300 rounded">
        <input type="number" name="gaji" placeholder="Gaji" class="p-2 border border-pink-300 rounded">
        <input type="number" name="rumah" placeholder="Tunjangan Rumah" class="p-2 border border-pink-300 rounded">
        <input type="number" name="tjabatan" placeholder="Tunjangan Jabatan" class="p-2 border border-pink-300 rounded">
        <input type="number" name="transport" placeholder="Tunjangan Transport" class="p-2 border border-pink-300 rounded">
        <button class="bg-pink-500 text-white py-2 rounded hover:bg-pink-600">SUBMIT</button>
    </form>

    <!-- DATA TABEL -->
    <div class="max-w-3xl mx-auto bg-white p-4 rounded shadow mt-6 border border-pink-300">
        <table class="w-full border text-sm">
            <thead class="bg-pink-600 text-white">
                <tr>
                    <th class="border p-2">NO</th>
                    <th class="border p-2">Nama</th>
                    <th class="border p-2">Jabatan</th>
                    <th class="border p-2">Partai</th>
                    <th class="border p-2">Gaji</th>
                    <th class="border p-2">T. Rumah</th>
                    <th class="border p-2">T. Jabatan</th>
                    <th class="border p-2">T. Transport</th>
                    <th class="border p-2">Edit</th>
                    <th class="border p-2">Hapus</th>
                </tr>
            </thead>
            <tbody>
                <?php
                require 'koneksi.php';
                $no = 1;

                function rp($angka){
                    return "Rp " . number_format($angka, 0, ',', '.');
                }

                $data = mysqli_query($conn, "SELECT * FROM gajidpr");

                while($row = mysqli_fetch_array($data)){
                    echo "
                    <tr class='hover:bg-pink-50'>
                        <td class='border p-2 text-center'>$no</td>
                        <td class='border p-2'>{$row['nama_anggota']}</td>
                        <td class='border p-2'>{$row['jabatan']}</td>
                        <td class='border p-2'>{$row['partai']}</td>
                        <td class='border p-2'>".rp($row['gaji_pokok'])."</td>
                        <td class='border p-2'>".rp($row['tunjangan_rumah'])."</td>
                        <td class='border p-2'>".rp($row['tunjangan_jabatan'])."</td>
                        <td class='border p-2'>".rp($row['tunjangan_transport'])."</td>

                        <td class='border p-2 text-center text-pink-600 font-semibold'>
                            <a href='edit.php?id={$row['id']}'>Edit</a>
                        </td>

                        <td class='border p-2 text-center text-red-600 font-semibold'>
                            <a href='delete.php?id={$row['id']}' onclick='return confirm(\"Apakah Anda yakin ingin menghapus?\")'>
                                Hapus
                            </a>
                        </td>
                    </tr>";
                    $no++;
                }
                ?>
            </tbody>
        </table>
    </div>

</body>
</html>
