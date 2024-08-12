<?php
$password = $_GET['password'] ?? '';
$view_source = $_GET['view_source'] ?? '';
$flag = file_get_contents('flag.txt');
$index_html = file_get_contents('index.html');


if ($view_source){
  echo highlight_file('index.php',true);
}else{
  echo $index_html;
}


if (base64_encode($password) === 'c3VwZXJzZWNyZXQ=') {
  echo $flag;
}else if ($password != ''){
  echo "<script>alert('wrong password!')</script>";
}

?>
