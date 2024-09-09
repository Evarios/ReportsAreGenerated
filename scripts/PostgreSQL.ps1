param (
    [string]$savePath,
    [string]$username,
    [string]$password,
    [string]$name
)

$env:PGPASSWORD = $password
pg_dump -U $username -s -f $savePath $name