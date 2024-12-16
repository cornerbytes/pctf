<?php 
ob_start();
session_start();
if (isset($_SESSION['login']) && $_SESSION['login']==true){
  echo "this time you need to get flag directly or indirectly from database. " . "<br>";
  echo "kurang dari 30 hari sudah masuk ke tahun 2025. Apa yang sudah kalian capai tahun ini ? apa target kalian tahun depan ??? ";
} else{ 
  header("Location: /index.php");
  die();
}
?>
