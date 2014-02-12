<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Carpool List</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <h1>Carpool</h1>
    <table>
      <tr>
        <th>Driver</th>
        <th>Date</th>
        <th>Total Days</th>
      </tr>
    %for row in rows:
      <tr>
        <td><a href="/update_driver/{{row[0]}}">{{row[0]}}</a></td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
      </tr>
    %end
    </table>
    <a href="/add_driver">Add Driver</a>
  </body>
</html>
