<!DOCTYPE html>
<html>
<head>
    <title>Survey Results</title>
    <style>
        table.data {
            width: 50%;
            margin: 20px auto;
            border-collapse: collapse;
        }
        table.data, table.data th, table.data td {
            border: 1px solid black;
        }
        table.data th, table.data td {
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Survey Results</h1>
    <div>
        <h2>Aggregated Data by Postcode</h2>
        {% for table in tables %}
            {{ table|safe }}
        {% endfor %}
    </div>
    <a href="/">Back to Survey</a>
</body>
</html>
