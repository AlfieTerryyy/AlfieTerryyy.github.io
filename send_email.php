<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $category = htmlspecialchars($_POST['category']);
    $priority = htmlspecialchars($_POST['priority']);
    $copy = isset($_POST['copy']) ? "Yes" : "No";
    $human = isset($_POST['human']) ? "Yes" : "No";
    $message = htmlspecialchars($_POST['message']);

    $to = 'alfie.terry1@mail.com';
    $subject = 'New Order Form Submission';
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    $body = "<html><body>";
    $body .= "<h2>Order Form Submission</h2>";
    $body .= "<p><strong>Name:</strong> $name</p>";
    $body .= "<p><strong>Email:</strong> $email</p>";
    $body .= "<p><strong>Category:</strong> $category</p>";
    $body .= "<p><strong>Priority:</strong> $priority</p>";
    $body .= "<p><strong>Copy to Email:</strong> $copy</p>";
    $body .= "<p><strong>I am a Human:</strong> $human</p>";
    $body .= "<p><strong>Message:</strong><br>$message</p>";
    $body .= "</body></html>";

    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Failed to send message.";
    }
} else {
    echo "Invalid request.";
}
?>
