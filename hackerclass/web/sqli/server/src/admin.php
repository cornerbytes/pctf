<?php 
ob_start();
session_start();
if (isset($_SESSION['login']) && $_SESSION['login']==true){
  $flag =  file_get_contents('flag.txt');
  echo $flag;
} else{ 
  header("Location: /index.php");
  die();
}
?>
