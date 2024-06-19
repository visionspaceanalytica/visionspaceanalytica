<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $email = $_POST["email"];
  $message = $_POST["message"];

  // Send the email using a secure SMTP server
  // Your SMTP configuration and email sending code goes here

  // Redirect the user to a thank you page
  header("Location: thankyou.html");
  exit();
}
?>
