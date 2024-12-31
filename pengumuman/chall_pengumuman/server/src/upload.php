<?php
// upload.php

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        echo "File upload failed with error code " . $file['error'];
        exit;
    }

    // Define the upload directory and file path
    $uploadDirectory = './uploads/';
    $uploadFilePath = $uploadDirectory . basename($file['name']);

    // Check if the directory exists, create it if not
    if (!is_dir($uploadDirectory)) {
        mkdir($uploadDirectory, 0777, true);
    }

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $uploadFilePath)) {
        echo "File uploaded successfully!";
    } else {
        echo "File upload failed!";
    }
} else {
    echo "No file uploaded.";
}
?>

