<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Delete Driver</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      li { list-style: none; }
    </style>
  </head>
  <body>
    <h2>Delete Driver</h2>
    <form action="del_driver" method="GET">
      <ul>
        %for driver in rows:
        <li><input type="radio" name="name" value="{{driver}}">{{driver}}</li>
        %end
      </ul>
      <input type="submit" name="delete" value="Delete">
    </form>
  </body>
</html>

