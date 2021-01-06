<#
    Gather list of current files and directories
    If it is a file, get the extension, and store file name
    If it is a folder, store folder name
    Look in folders and repeat recursively
    Parameter for how many levels you want to explore
#>


function Get-ChildStructure {
    param(
        [Parameter(Mandatory=$false)]
        [String]$Depth = 1,
        [Parameter(Mandatory=$false)]
        [String]$Path
    )

    $arrayDefaultPath = $Path.Split("\")
    $arrayDefaultPathLength = $arrayDefaultPath.Length

    $row = 0
    $Files = Get-ChildItem -Path $Path -Depth $Depth | Sort-Object FullName
    foreach ($Item in $Files) {
        $fileFullName = $item.FullName
        $fileExtension = [System.IO.Path]::GetExtension($Item.Name)
        $trimFileExtension = $fileExtension.Replace(".","")
        $arrPath = $fileFullName.Split("\")
        $pathLength = $arrPath.Length
        if ( (Test-Path -Path $fileFullName -PathType Container) -eq $true ) {
            $indentCount = $pathLength-$arrayDefaultPathLength
            [String]$Indent = "=="*$indentCount+"> "
            Write-Host "||" -ForegroundColor Red
            Write-Host "||"$Indent -ForegroundColor Red -NoNewline
            Write-Host " DIR" -ForegroundColor Blue -NoNewline
            Write-Host " "$Item.Name
        }
        elseif ( (Test-Path -Path $fileFullName -PathType Leaf) -eq $true ) {
            $indentCount = $pathLength-$arrayDefaultPathLength
            [String]$Indent = ("=="*($indentCount)+"> ")
            Write-Host "||"$Indent -ForegroundColor Green -NoNewline
            Write-Host $trimFileExtension -ForegroundColor Blue -NoNewline
            Write-Host " "$Item.Name
        }

    }

}

Get-ChildStructure -Path C:\Users\imser -Depth 2