Create venv
```powershell
# mkdir .venv
# pip install venv
python -m venv \.venv
```


Loading a.venv in microsoft powershell
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser && 
./.venv/Scripts/Activate.ps1
```