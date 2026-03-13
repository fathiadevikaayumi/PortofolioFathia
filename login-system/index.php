<!DOCTYPE html>
<html>
<head>
    <title>Halaman Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Silahkan Login</h2>

        <form action="proses_login.php" method="POST">
            <label>Username</label>
            <input type="text" name="username" required>

            <label>Password</label>
            <input type="password" name="password" required>

            <button type="submit">LOGIN</button>
        </form>

        <p>Belum punya akun?
            <a href="registrasi.php">Daftar dulu di sini</a>
        </p>
    </div>

</body>
</html>
