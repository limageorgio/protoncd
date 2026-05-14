$files = @(
    '_tmp_fix_playground_canonicals.py',
    '_tmp_fix_playground_canonicals.ps1',
    '_tmp_check_playground_canonicals.ps1',
    '_tmp_commit_playground_canonicals.ps1',
    '_cleanup_final.bat',
    '_cleanup_tmp.py',
    'remove_tmp_files.py'
)

$cwd = Get-Location
foreach ($file in $files) {
    $path = Join-Path $cwd $file
    if (Test-Path $path) {
        try {
            Remove-Item $path -Force -ErrorAction Stop
            Write-Host "REMOVED: $file"
        } catch {
            Write-Host "ERROR: $file - $_"
        }
    } else {
        Write-Host "NOT_FOUND: $file"
    }
}

Write-Host "CLEANUP_COMPLETE"
