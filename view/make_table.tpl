<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Carpool List</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
      table {
        border-collapse: collapse;
      }
      table td, th {
        border: 1px solid #999;
        padding: .5em;
        text-align: center;
      }
    </style> 
  </head>
  <body>
    <h2>Carpool</h2>
    <table>
      <tr>
        <th>Driver</th>
        <th>Date</th>
      </tr>
      %for row in rows:
      <tr>
        <td><a href="/update_driver/{{row[0]}}">{{row[0]}}</a></td>
        <td>{{row[1]}}</td>
      </tr>
      %end
    </table>
  </body>
</html>
