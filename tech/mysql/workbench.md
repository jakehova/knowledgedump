# Retrieving passwords from local vault: 

Add-Type -AssemblyName System.Security

$cipher = Get-Content %APPDATA%\MySQL\Workbench\workbench_user_data.dat -Encoding Byte

$scope = [System.Security.Cryptography.DataProtectionScope]::CurrentUser

$mysqlpwd = [System.Security.Cryptography.ProtectedData]::Unprotect($cipher, $null, $scope )

[System.Text.UTF8Encoding]::UTF8.GetString($mysqlpwd)