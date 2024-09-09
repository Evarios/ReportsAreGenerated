$envFilePath = "../.env"

# Loading file
$envContent = Get-Content $envFilePath

foreach ($line in $envContent) {
    # Continue if line is empty or starts with #
    if (-not [string]::IsNullOrWhiteSpace($line) -and -not $line.StartsWith("#")) {
        # Split line by "="
        $key, $value = $line -split "=", 2

        # Set environment variable
        [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::User)
    }
}

# Start PostgreSQL
pg_dump -U $env:USERNAME -s -f ../metadata/metadata.sql $env:DATABASE