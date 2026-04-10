$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$docsRoot = Join-Path $repoRoot 'docs'

$allowedRootFiles = @('index.md')
$allowedRootDirs = @(
  'foundations',
  'essays',
  'forge-diaries',
  'outward',
  'policies',
  'vcof',
  'casebooks'
)

if (-not (Test-Path -LiteralPath $docsRoot)) {
  Write-Error "docs/ directory not found at $docsRoot"
  exit 1
}

$items = Get-ChildItem -LiteralPath $docsRoot -Force
$rootFiles = $items | Where-Object { -not $_.PSIsContainer }
$rootDirs = $items | Where-Object { $_.PSIsContainer }

$unexpectedFiles = $rootFiles | Where-Object { $_.Name -notin $allowedRootFiles }
$unexpectedDirs = $rootDirs | Where-Object { $_.Name -notin $allowedRootDirs }
$missingFiles = $allowedRootFiles | Where-Object { -not (Test-Path -LiteralPath (Join-Path $docsRoot $_)) }
$missingDirs = $allowedRootDirs | Where-Object { -not (Test-Path -LiteralPath (Join-Path $docsRoot $_)) }

if ($unexpectedFiles -or $unexpectedDirs -or $missingFiles -or $missingDirs) {
  Write-Host 'docs/ structure guardrail failed.' -ForegroundColor Red

  if ($unexpectedFiles) {
    Write-Host 'Unexpected files in docs/ root:' -ForegroundColor Yellow
    $unexpectedFiles | ForEach-Object { Write-Host "  - $($_.Name)" }
  }

  if ($unexpectedDirs) {
    Write-Host 'Unexpected directories in docs/ root:' -ForegroundColor Yellow
    $unexpectedDirs | ForEach-Object { Write-Host "  - $($_.Name)" }
  }

  if ($missingFiles) {
    Write-Host 'Missing required root files:' -ForegroundColor Yellow
    $missingFiles | ForEach-Object { Write-Host "  - $_" }
  }

  if ($missingDirs) {
    Write-Host 'Missing required root directories:' -ForegroundColor Yellow
    $missingDirs | ForEach-Object { Write-Host "  - $_" }
  }

  exit 1
}

Write-Host 'docs/ structure guardrail passed.' -ForegroundColor Green
