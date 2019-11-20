<html>

	<head>
		<title > OTTO2019 Test Viewing Page </title>
		<meta charset="utf-8" />
		<style type="text/css">
			#header{
				margin: 20px;
				padding: 20px;
				border: 1px solid #828282;
			}
			#section{
				margin: 20px 20px 20px 20px;
				padding: 20px;
				border: 1px solid #828282;
			}
			#footer{
				clear: both;
				margin: 20px;
				padding: 20px;
				border: 1px solid #828282;
			}
		</style>
	</head>

	<body>
		<div id="header">
			<h2 align="center"> OTTO2019 Test Viewing Page  </h2>
			<hr style="border: solid 2px black;">
		</div>

		<div id="section">
			<h3> TSN LIST </h3>
			<ul>
			%for line in lines:
			<li>{{line}}</li>
			%end
			</ul>
		</div>
		
		<div id ="footer">
			<b>footer</b>
			<p>CopyRight</p>
		</div>
	</body>
</html>

