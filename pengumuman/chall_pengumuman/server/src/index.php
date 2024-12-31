<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- hint : jika kamu sudah mendapatkan hak akses server remote code execution cari file announcement.txt di folder root /  -->
    <title>Pengumuman PCT</title>
    <style>
        body {font-family: 'Roboto', sans-serif;margin: 0;padding: 0;display: flex;justify-content: center;align-items: center;height: 100vh;background: #f0f4f8;color: #333;}
        .container {text-align: center;background: white;border-radius: 12px;padding: 40px;box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);width: 80%;max-width: 600px;}
        h1 {font-size: 2rem;color: #333;margin-bottom: 20px;}
        .drag-drop-area {border: 2px dashed #4A90E2;padding: 40px;border-radius: 8px;cursor: pointer;transition: all 0.3s ease;margin-bottom: 20px;}
        .drag-drop-area:hover {background-color: #f0f4f8;border-color: #0061f2;}
        .upload-btn {display: inline-block;padding: 12px 30px;background: #4A90E2;color: white;border-radius: 30px;font-size: 16px;text-transform: uppercase;cursor: pointer;transition: background 0.3s ease;}
        .upload-btn:hover {background: #0061f2;}
        .file-name {margin-top: 10px;color: #666;font-size: 14px;}
        input[type="file"] {display: none;}
    </style>
</head>
<body>
<div class="container">
    <h1>Cek kelulusan <i>PCT</i> </h1><h2>upload your file here</h2>
    <div id="drop-area" class="drag-drop-area">
        Drag & Drop your file here or
        <label for="file-upload" class="upload-btn">Browse</label>
    </div>
    <input type="file" id="file-upload">
    <div id="file-name" class="file-name"></div>
    
    <form id="upload-form" action="/upload.php" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="MAX_FILE_SIZE" value="10485760" /> 
        <input type="file" name="file" id="hidden-file" />
        <button type="submit" class="upload-btn" style="display:none;" id="submit-btn">Upload</button>
    </form>
</div>

<script>
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("file-upload");
    const hiddenFileInput = document.getElementById("hidden-file");
    const fileNameDiv = document.getElementById("file-name");
    const submitBtn = document.getElementById("submit-btn");
    const form = document.getElementById("upload-form");
    dropArea.addEventListener("dragover", function (e) {
        e.preventDefault();
        dropArea.style.backgroundColor = "#f0f4f8";
    });

    dropArea.addEventListener("dragleave", function () {
        dropArea.style.backgroundColor = "transparent";
    });

    dropArea.addEventListener("drop", function (e) {
        e.preventDefault();
        dropArea.style.backgroundColor = "transparent";
        const file = e.dataTransfer.files[0];
        if (file) {
            fileNameDiv.textContent = `Selected: ${file.name}`;
            hiddenFileInput.files = e.dataTransfer.files;
            submitBtn.style.display = "inline-block";
        }
    });
    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (file) {
            fileNameDiv.textContent = `Selected: ${file.name}`;
            hiddenFileInput.files = fileInput.files;
            submitBtn.style.display = "inline-block";
        }
    });
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.open("POST", form.action, true);

        xhr.onload = function () {
            if (xhr.status === 200) {
                alert("File uploaded successfully!\nplease visit /uploads/your_file_name !");
            } else {
                alert("File upload failed!");
            }
        };

        xhr.send(formData);
    });
</script></body></html>