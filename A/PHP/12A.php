<?php
  $fr = fopen("php://stdin", "r");
  $fw = fopen("php://stdout", "w");

  fscanf($fr, "%s", $r1);
  fscanf($fr, "%s", $r2);
  fscanf($fr, "%s", $r3);   
  
  function chk()
  {
    global $r1, $r2, $r3;
    return ($r1[0] == $r3[2]) &&
           ($r1[1] == $r3[1]) && 
           ($r1[2] == $r3[0]) &&
           ($r2[0] == $r2[2]);
  }
  
  if (chk())
  {
    fprintf($fw, "YES");
  }
  else
  {
    fprintf($fw, "NO");
  }
   
  fclose($fr);
  fclose($fw);
?>