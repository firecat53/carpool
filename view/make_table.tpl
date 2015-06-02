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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $('.checkbox').on('change',function(){
                var selected = $("#riders input:checked").map(function(i, el) {
                    return el.value;}).get();
                $.ajax({
                    type: 'POST',
                    url: '/updateRiders',
                    data: { selected }
                });
            });
        });
    </script>
  </head>
  <body>
    <h2>Carpool</h2>
    <h3>Check the box if you are carpooling on <span id="date">{{shift}}</span></h3>
    <form id="riders" method="post" action="/updateRiders" autocomplete="off">
        <table>
        <tr>
            <th>Driver</th>
            <th>Date</th>
        </tr>
        %for row in rows:
        <tr>
            <td><a href="/update_driver/{{row[0]}}">{{row[0]}}</a></td>
            <td>{{row[1]}}</td>
            <td><input type="checkbox" class="checkbox" name="rider" value="{{row[0]}}" {{'checked=""' if row[4] == 1 else ""}} /></td>
        </tr>
        %end
        </table>
    </form>
  </body>
</html>
