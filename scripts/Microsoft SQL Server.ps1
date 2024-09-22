param (
    [string]$savePath,
    [string]$username,
    [string]$password,
    [string]$name,
    [string]$serverInstance
)

# Get db schema query
$query = @"
SET NOCOUNT ON;
SELECT 
    'CREATE TABLE ' + s.name + '.' + t.name + ' (' +
    STUFF((SELECT ', ' + c.name + ' ' + 
                CASE 
                    WHEN c.is_identity = 1 THEN 'IDENTITY(1,1) ' + ty.name
                    ELSE ty.name
                END +
                CASE 
                    WHEN ty.name IN ('char', 'varchar', 'nchar', 'nvarchar') THEN '(' + IIF(c.max_length = -1, 'MAX', CAST(c.max_length AS VARCHAR(10))) + ')'
                    WHEN ty.name IN ('decimal', 'numeric') THEN '(' + CAST(c.precision AS VARCHAR(10)) + ', ' + CAST(c.scale AS VARCHAR(10)) + ')'
                    ELSE ''
                END +
                CASE 
                    WHEN c.is_nullable = 1 THEN ' NULL' 
                    ELSE ' NOT NULL' 
                END
           FROM sys.columns c
           JOIN sys.types ty ON c.user_type_id = ty.user_type_id
           WHERE c.object_id = t.object_id
           ORDER BY c.column_id
           FOR XML PATH('')), 1, 2, '') + ');'
FROM sys.tables t
JOIN sys.schemas s ON t.schema_id = s.schema_id;
"@

# Execute query
$result = Invoke-Sqlcmd -ServerInstance $serverInstance -Database $name -Query $query -Username $username -Password $password | Out-String -Width 4096

# Save result to file
$result | Out-File -FilePath $savePath 

# Remove first 3 lines
$file = Get-Content $savePath
$file = $file | Select-Object -Skip 3
$file | Set-Content $savePath
