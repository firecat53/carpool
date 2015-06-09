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
      #date {
        background: yellow;
        color: black;
      }
    </style> 
  </head>
  <body>
    <h2>Carpool</h2>
    <h3>Check the box if you are carpooling on <span id="date">{{shift}}</span></h3>
        <table>
            <thead>
                <tr>
                <th>Driver</th>
                <th>Date</th>
                </tr>
            </thead>
            %for row in rows:
            <tr>
                <td><a href="/update_driver/{{row[0]}}">{{row[0]}}</a></td>
                <td>{{row[1]}}</td>
                <td><a href="/update_rider/{{row[0]}}">
                      <img src="static/{{'in.png' if row[4] else 'out.png'}}" />
                    </a>
                </td>
            </tr>
            %end
        </table>
  </body>
</html>
