# orc

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

This was really challenging. At first, I thought the catch is in the `addslashes` function. Here is some articles that I've read:

 1. [https://www.php.net/manual/en/function.addslashes.php](https://www.php.net/manual/en/function.addslashes.php)
 2. [https://shiflett.org/blog/2006/addslashes-versus-mysql-real-escape-string](https://shiflett.org/blog/2006/addslashes-versus-mysql-real-escape-string)

They say that `addslashes` is vulnerable, so I tried following it. Didn't work. Reading it again, I know that somehow my input password has to be the same as the password in the database. At some point I gave up and watched a [youtube video](https://youtu.be/6U5a87Ayrc8?si=4lNTnaCDzO2yRnDl). I watched it for 30 seconds where he says that it involves "Blind SQL Injection". Here is some articles that I read:

 1. [https://owasp.org/www-community/attacks/Blind_SQL_Injection](https://owasp.org/www-community/attacks/Blind_SQL_Injection)

After reading the article, it seems like the way is too bruteforce the admin password. So I tried bruteforcing it using a python script. In the end, I got the password by bruteforcing it.