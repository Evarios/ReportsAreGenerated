param (
    [string]$savePath,
    [string]$username,
    [string]$password,
    [string]$name
)

$env:MYSQL_PWD = $password
mysqldump -u $username --no-data $name > $savePath