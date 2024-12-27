<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Foydalanuvchidan kelgan ma'lumotlarni olish
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $date = htmlspecialchars($_POST['date']);
    $time = htmlspecialchars($_POST['time']);
    $people = htmlspecialchars($_POST['people']);
    $message = htmlspecialchars($_POST['message']);

    // Email yuborish yoki boshqa protsedura
    // Masalan, email yuborishni yoki ma'lumotni saqlashni amalga oshirish

    // Muvaqqat muvaffaqiyatli xabar
    header('Location: book-a-table.php?status=success');
    exit;
}
?>
