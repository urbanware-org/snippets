# eicarxt

Simple *PowerShell* code to "extract" the *EICAR* anti-malware testfile stored
as *Base64* string into the directory where this *PowerShell* script file
is located.

So, you can always store and keep the *EICAR* anti-malware test file on e.g. removable media without downloading (and "losing") it again and again due to the taken action of the anti-virus software.

## Usage

Just run the script file inside the *PowerShell* console

```powershell
./eicarxt.ps
```

which will create the file `eicar.com` inside the directory where the script is being run. After that your anti-virus software should raise an alert and depending on that program initiate further actions.
