# Test-LogAnalyzer.ps1

# Set the URL of the local LLM log analysis API
$apiUrl = "http://localhost:5001/analyze"

# Define a test log payload
$payload = @{
    log = @(
        "Failed SSH login attempt from 192.168.1.100",
        "New user created: evil_user",
        "Unexpected sudo access granted to john"
    )
} | ConvertTo-Json -Depth 3

# Optional: Write the payload to console
Write-Host "Sending JSON payload:"
Write-Host $payload

# Send the POST request
try {
    $response = Invoke-RestMethod -Uri $apiUrl -Method Post -Body $payload -ContentType "application/json"
    Write-Host "`n✅ Response received:`n"
    $response | ConvertTo-Json -Depth 4
}
catch {
    Write-Host "`n❌ Error connecting to the API:`n"
    Write-Error $_
}
