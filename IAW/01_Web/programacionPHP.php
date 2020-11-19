<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Hola mundo!</title>
    <link rel="stylesheet" href="css/estiloPrincipal.css">
    <script defer src="js/programacionCliente.js"></script>
  </head>
  <body>
    <h1>Hola mundo!</h1>
    <?php
      // phpinfo();

      function color(){
        return sprintf('#%06X', mt_rand(0, 0xFFFFFF));
      }

      for($i = 0; $i< 10; $i++){
        echo "<span style='background-color: ".color()."''> hola </span>";
      }
    ?>
  </body>
</html>
