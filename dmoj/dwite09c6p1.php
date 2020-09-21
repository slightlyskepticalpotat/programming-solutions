<?php
for ($i = 0; $i < 5; $i++) {
    $string = fgets(STDIN);
    echo str_rot13($string);
}
?>