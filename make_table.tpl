%#Template to generate an HTML table for all the drivers in the database
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
