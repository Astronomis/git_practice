Function New-CoCDBEntry {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [String]$Building,
        [Parameter(Mandatory=$true)]
        [String]$Level,
        [Parameter(Mandatory=$true)]
        [String]$MaxLevel,
        [Parameter(Mandatory=$true)]
        [String]$ResourceType,
        [Parameter(Mandatory=$true)]
        [String]$Storage,
        [Parameter(Mandatory=$true)]
        [String]$Income,
        [Parameter(Mandatory=$true)]
        [String]$UpgradeResource,
        [Parameter(Mandatory=$true)]
        [String]$UpgradeCost,
        [Parameter(Mandatory=$true)]
        [String]$Count
    )
        #Create our Building Object    
        $Output = New-Object -TypeName PSCustomObject -Property @{
            Building        = $Building
            BuildingCount   = $Count
            Level           = $Level
            MaxLevel        = $MaxLevel
            ResourceType    = $ResourceType
            Storage         = $Storage
            Income          = $Income
            UpgradeResource = $UpgradeResource
            UpgradeCost     = $UpgradeCost
        }
        #Export Object to CSV file for long term data storage.
        $Output | 
            Select-Object Building,Count,Level,MaxLevel,ResourceType,Storage,Income,UpgradeResource,UpgradeCost | 
            Export-Csv -Path $env:USERPROFILE\Documents\CoCDB.csv -Append -NoTypeInformation
        #Return output to variable or to console.
        return $Output | Select-Object Building,BuildingCount,Level,MaxLevel,ResourceType,Storage,Income,UpgradeResource,UpgradeCost
    }

Function Get-CoCCurrentStatus {
    [CmdletBinding()]
    $Buildings = Import-Csv -Path $env:USERPROFILE\Documents\CocDB.csv
    $Buildings | ft
    #Calculate Gold/Mana Storage/Income
    $GoldIncome = 0
    $GoldStorage = 0
    $ManaIncome = 0
    $ManaStorage = 0
    $TotalGoldUpgradeCost = 0
    $TotalManaUpgradeCost = 0
    foreach ($Building in $Buildings){
        if ($Building.ResourceType -like "*Gold*") {
            $GoldIncome += ([int]$Building.Income*[int]$Building.BuildingCount)
            $GoldStorage += ([int]$Building.Storage*[int]$Building.BuildingCount)
            
        }
        elseif ($Building.ResourceType -like "*Mana*") {
            $ManaIncome += ([int]$Building.Income*[int]$Building.BuildingCount)
            $ManaStorage += ([int]$Building.Storage*[int]$Building.BuildingCount)
        }
        else {Continue}
        if ($Building.UpgradeResource -like "*Gold*") {
            $TotalGoldUpgradeCost += ([int]$Building.UpgradeCost*[Int]$Building.BuildingCount)
        }
        elseif ($Building.UpgradeResource -like "*Mana*") {
            $TotalManaUpgradeCost += ([int]$Building.UpgradeCost*[Int]$Building.BuildingCount)
        }
        
    }
    
    $DailyGoldIncome = $GoldIncome*24
    $DailyManaIncome = $ManaIncome*24
    $DaysToSaveGold = [Math]::Floor([int]$TotalGoldUpgradeCost/[int]$DailyGoldIncome)
    $DaysToSaveMana = [Math]::Floor([int]$TotalManaUpgradeCost/[int]$DailyManaIncome)
    $Output = New-Object -TypeName PSCustomObject @{
        HourlyGoldIncome = '{0:C}' -f $GoldIncome
        DailyGoldIncome = '{0:C}' -f $DailyGoldIncome
        TotalGoldStorage = '{0:C}' -f $GoldStorage
        HourlyManaIncome = '{0:C}' -f $ManaIncome
        DailyManaIncome = '{0:C}' -f $DailyManaIncome
        TotalManaStorage = '{0:C}' -f $ManaStorage
        TotalGoldUpgradeCost = '{0:C}' -f $TotalGoldUpgradeCost
        TotalManaUpgradeCost = '{0:C}' -f $TotalManaUpgradeCost
        DaysToSaveGold = $DaysToSaveGold
        DaysToSaveMana = $DaysToSaveMana
    }
    return $Output
}

Function Get-CoCBuildings {
    [CmdletBinding()]

    $Buildings = Import-Csv -Path $env:USERPROFILE\Documents\CoCDB.csv
    return $Buildings | Sort-Object ResourceType,Buidling,Level
} 