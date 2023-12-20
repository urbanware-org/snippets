# eicarxt

Simple *PowerShell* code to create the *EICAR* anti-malware testfile stored as *Base64* string.

So, you can always store and keep the *EICAR* anti-malware test file on e.g. removable media without downloading (and "losing") it again and again due to the taken action of the anti-virus software.

## Usage

Just run the script file inside the *PowerShell* console

```powershell
./eicarxt.ps1
```

which will then "extract" the *EICAR* anti-malware testfile stored as a *Base64* string by decoding and writing it into the file `eicar.com` inside the directory from where the script file is being run.

After that, the real-time protection of your anti-virus software should raise an alert and/or remove the file.
