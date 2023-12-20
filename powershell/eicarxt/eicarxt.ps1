# Simply run this script file inside the PowerShell console which will then
# "extract" the EICAR anti-malware testfile stored as a Base64 string by
# decoding and writing it into the file 'eicar.com' inside the directory from
# where the script file is being run.
#
# After that, the real-time protection of your anti-virus software should
# raise an alert and/or remove the file.

$eicar = "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo="
Write-Host "Extracting anti-malware testfile content to 'eicar.com'."
[Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($eicar)) | Out-File "eicar.com"
