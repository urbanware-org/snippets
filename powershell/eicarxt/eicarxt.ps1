# Simply run this script which will "extract" the EICAR anti-malware testfile
# stored as Base64 string into the directory where this PowerShell script file
# is located.
#
# This will create the file 'eicar.com' inside the directory where the script
# is being run. After that your anti-virus software should raise an alert and
# depending on that program initiate further actions.

$eicar = "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo="
Write-Host "Extracting anti-malware testfile content to 'eicar.com'."
[Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($eicar)) | Out-File "eicar.com"
