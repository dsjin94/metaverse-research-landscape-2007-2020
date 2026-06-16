param(
    [string]$FiguresPath = ".\outputs\figures",
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"

$resolvedPath = Resolve-Path -LiteralPath $FiguresPath
Write-Host "Figures folder: $resolvedPath"

$files = Get-ChildItem -LiteralPath $resolvedPath -File |
    Where-Object { $_.Extension.ToLower() -in @(".jpg", ".jpeg", ".png") }

if (-not $files) {
    throw "No JPG, JPEG, or PNG files were found in: $resolvedPath"
}

$planned = foreach ($file in $files) {
    if ($file.BaseName -notmatch '(?<!\d)(20(?:0[7-9]|1[0-9]|20))(?!\d)') {
        Write-Warning "Skipped because no year from 2007 to 2020 was found: $($file.Name)"
        continue
    }

    $year = $Matches[1]
    $extension = $file.Extension.ToLower()

    # Normalize .jpg to .jpeg so all current files use one consistent extension.
    if ($extension -eq ".jpg") {
        $extension = ".jpeg"
    }

    [PSCustomObject]@{
        SourceFile = $file
        Year       = $year
        NewName    = "metaverse_landscape_$year$extension"
    }
}

$duplicates = $planned | Group-Object Year | Where-Object Count -gt 1
if ($duplicates) {
    Write-Host ""
    Write-Host "Multiple files were found for the same year. No files were renamed." -ForegroundColor Red
    foreach ($group in $duplicates) {
        Write-Host "Year $($group.Name):" -ForegroundColor Yellow
        $group.Group.SourceFile.Name | ForEach-Object { Write-Host "  $_" }
    }
    throw "Resolve duplicate-year files first, then run the script again."
}

Write-Host ""
Write-Host "Planned renames:" -ForegroundColor Cyan
foreach ($item in $planned | Sort-Object Year) {
    Write-Host ("  {0}  ->  {1}" -f $item.SourceFile.Name, $item.NewName)
}

if ($WhatIf) {
    Write-Host ""
    Write-Host "WhatIf mode: no files were changed." -ForegroundColor Yellow
    exit 0
}

foreach ($item in $planned) {
    $targetPath = Join-Path $resolvedPath $item.NewName

    if ((Test-Path -LiteralPath $targetPath) -and
        ($item.SourceFile.FullName -ne $targetPath)) {
        throw "Target file already exists: $targetPath"
    }

    Rename-Item -LiteralPath $item.SourceFile.FullName -NewName $item.NewName
}

Write-Host ""
Write-Host "Renaming completed successfully." -ForegroundColor Green
Write-Host "Run 'git status' to review the renamed files before committing."
