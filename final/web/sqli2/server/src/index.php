<?php
ob_start();
session_start();

$view_source = $_GET['view_source'] ?? '';
$flag = file_get_contents('flag.txt');
$index_html = file_get_contents('index.html');


if ($view_source){
  echo highlight_file('index.php',true);
}else{
  echo $index_html;
}

function set_cookie($value){
  $_SESSION['login'] = $value;
}

// this code look ugly 
function query_database($username){
  $db = new PDO("sqlite:database.db");
  $query = "SELECT * FROM userdata where USERNAME ='{$username}'";
  $result =  $db->query($query);
  if ($result === false) {
    return false;
  }
  $result = $result->fetch();
  if ($result) {
    return $result;
  } else {
    return false;
  }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = $_POST["username"];
  $password = $_POST["password"];
  $data = query_database($username);

    
  if ($data) {
    if ($password === $data['password']) {
      set_cookie(true);
      header("Location: /admin.php");
      die();
    } else {
      echo "wrong password";
    }
  } else {
    echo "data not found";
  }
}


?>
