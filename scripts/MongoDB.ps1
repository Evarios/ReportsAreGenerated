param (
    [string]$savePath,
    [string]$username,
    [string]$password,
    [string]$name,
    [string]$hostname,
    [string]$port
)

$authUri = "mongodb://${username}:${password}@${hostname}:${port}/${name}?authSource=admin"

# Fetch the collection names using a single mongosh command and parse JSON output
$collections = (& mongosh $authUri --eval "JSON.stringify(db.getCollectionNames())" | ConvertFrom-Json)

foreach ($collection in $collections) {
    Write-Host "Processing collection: $collection"

    $mongoshOutput = & mongosh $authUri --eval "var collection = '$($collection)'" variety.js

    # Process output to skip the first 19 lines
	$processedOutput = $mongoshOutput | Select-Object -Skip 18
	Write-Output "Processing collection: $collection" | Out-File -FilePath $savePath -Append

    $processedOutput | Out-File -FilePath $savePath -Append

    # Optional: You can also log processed collection names to a separate file if desired
    # Write-Host "Processed collection: $collection" | Out-File -FilePath $savePath -Append
}

# Write-Host "Processed data saved to $savePath"


