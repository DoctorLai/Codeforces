<?php
  $fr = fopen("php://stdin", "r");
  //$fw = fopen("php://stdout", "w");
 
  fscanf($fr, "%d", $n);
  $n *= 2;
  $k = (int)sqrt($n);
  $found = false;
  for ($i = 1; $i < $k; $i ++)
  {
    $r = $n - $i * $i - $i;
    $x = (int)sqrt($r);
    if ($x * ($x + 1) == $r)
    {
      $found = true;
      break;
    }
  }
  if ($found)
  {
    //fprintf($fw, "YES");
    echo "YES";
  }
  else
  {
    //fprintf($fw, "NO");
    echo "NO";
  }
  fclose($fr);
  //fclose($fw);
?>