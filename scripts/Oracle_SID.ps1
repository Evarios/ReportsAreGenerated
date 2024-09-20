param (
    [string]$savePath,
    [string]$username,
    [string]$password,
    [string]$name,
    [string]$hostname,
    [string]$port
)


$query = @"
SET LONG 5000
SET PAGESIZE 0
SET LINESIZE 1000
SELECT DBMS_METADATA.GET_DDL('TABLE', table_name, '$username') AS schema 
FROM all_tables 
WHERE owner = '$username';
EXIT;
"@

# Connection URL
$connectionString = "$username/$password@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=$hostname)(PORT=$port))(CONNECT_DATA=(SID=$name)))"

# Temp file for SQL query
$sqlFilePath = "query.sql"
$query | Out-File -FilePath $sqlFilePath -Encoding ASCII

# Fetch schema
$result = & sqlplus -S $connectionString "@" $sqlFilePath

# Remove temp file
Remove-Item -Path $sqlFilePath

# Process the result
$processedData = $result -replace '\n', ' ' -replace '\t', ' ' -replace '     ', ' ' -replace '   ', ' ' | 
ForEach-Object {
    if ($_ -match "CREATE TABLE") {
        "; $_"
    }
    else {
        "$_"
    }
}

# Save file
$processedData | Out-File -FilePath $savePath 