<!DOCTYPE html>
<html>
  <head>
    <title>Command</title>
  </head>
  <body>
    <div class="container" align="center">
      <h1>I think there is a vuln here!</h1>
      <form action="index.php" method="GET">
        <label>Name:</label>
        <input type="text" name="typeBox" value=""><br>
        <input type="submit" value="Submit">
      </form>
    </div>
    <div class="result" align="center">
      <?php
      if(isset($_GET["typeBox"])){
        $target = $_GET["typeBox"];
        echo shell_exec($target);
      }
      ?>
    </div>
  </body>
</html>
