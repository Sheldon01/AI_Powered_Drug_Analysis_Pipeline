# Path to the folder containing files and checksums.txt
$folderPath = "C:\Users\sheld\Downloads\ChemblFiles"
$checksumFilePath = "$folderPath\checksums.txt"

# Read and parse the checksums.txt file
$expectedHashes = Get-Content $checksumFilePath | ForEach-Object {
    $split = $_ -split '\s+', 2
    if ($split.Count -eq 2) {
        [PSCustomObject]@{
            Hash = $split[0].Trim()
            File = $split[1].Trim()
        }
    }
}

# Debug: Output the parsed expected hashes
Write-Host "Parsed expected hashes:"
$expectedHashes | ForEach-Object { Write-Host "$($_.Hash) - $($_.File)" }

# Only process files listed in checksums.txt
$expectedHashes | ForEach-Object {
    $filePath = Join-Path -Path $folderPath -ChildPath $_.File

    if (Test-Path -Path $filePath) {
        $actualHash = Get-FileHash -Path $filePath -Algorithm SHA256
        if ($actualHash.Hash -eq $_.Hash) {
            Write-Host "Match: $($_.File)"
        } else {
            Write-Host "Mismatch: $($_.File)"
        }
    } else {
        Write-Host "File not found: $($_.File)"
    }
}
