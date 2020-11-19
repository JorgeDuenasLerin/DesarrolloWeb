<?php


try {
    $db_name="gestionaplus";
    $db_user = "gestionaplus";
    $db_pass = "1234";
    $mbd = new PDO("mysql:host=localhost;dbname=$db_name", $db_user, $db_pass);

    // Utilizar la conexión aquí
    $resultado = $mbd->query('SELECT * FROM Frutas');




    // Ya se ha terminado; se cierra
    $mbd = null;

} catch (PDOException $e) {
    print "¡Error!: " . $e->getMessage() . "\n";
    die();
}

?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Conexión DB</title>
    <style media="screen">
      table, td, th {
        border: 1px solid black;
        border-collapse: collapse;
        padding: 3px 1.1em;
      }
    </style>
  </head>
  <body>
    <h1>Listado de base de datos</h1>
    <table>
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Precio</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($resultado as $fila){ ?>
          <tr>
              <td><?=$fila[1]?></td>
              <td><?=$fila[2]?></td>
          </tr>
        <?php } ?>
      </tbody>
    </table>
  </body>
</html>
