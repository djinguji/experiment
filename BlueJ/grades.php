<?php
// open the database connection
$mysqli = new mysqli('localhost', 'jingujin_shared', 'ad320-shared', 'jingujin_testing');
if($mysqli->connect_error) {
	die('Connect error ('.$mysqli->connect_errno.') '.$mysqli->connect_error);
}

$msg = "Success ... $mysqli->host_info.<br/>";

//$query = 'INSERT INTO grades VALUES (456, 10004, \'B\');';

//if($mysqli->query($query)) {
//	$msg .= 'Success ... added to grades<br/>';
//}

$query = 'SELECT students.name AS student, grades.grade, courses.name AS course FROM grades JOIN (students, courses) ON (students.id = student_id AND course_id = courses.id) order by course';

if($result = $mysqli->query($query)) {
	$msg .= "Success ... $result->num_rows rows returned using the new account.";
}

$mysqli->close();
?>
<!doctype html>
<html>
	<head>
		<title>MySQL Test Page</title>
		<meta charset='utf-8'>
	</head>
	<body>
		<p><?= $msg ?></p>
		<table cellpadding=2 border=1>
			<tr>
				<th>Student</th>
				<th>Course</th>
				<th>Grade</th>
			</tr>
<?php
	while($row = $result->fetch_assoc()) {
?>
			<tr>
				<td><?= $row['student'] ?></td>
				<td><?= $row['course'] ?></td>
				<td><?= $row['grade'] ?></td>
			</tr>
<?php	
	}
	$result->close();
?>			
	</body>
</html>
