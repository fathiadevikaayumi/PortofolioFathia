<!DOCTYPE html>
<html>
<head>
    <title>Registrasi</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Silahkan Registrasi</h2>

        <form action="proses_registrasi.php" method="POST">
            <label>Username</label>
            <input type="text" name="username" required>

            <label>Password</label>
            <input type="password" name="password" required>

            <label>Role</label>
            <select name="role" required>
                <option value="">-- Pilih Role --</option>
                <option value="user">User</option>
                <option value="admin">Admin</option>
            </select>

            <button type="submit">DAFTAR</button>
        </form>

        <p>Sudah punya akun?
            <a href="index.php">Login</a>
        </p>
    </div>

</body>
</html>
