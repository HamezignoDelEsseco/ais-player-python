# Objective
The goal is to build a dummy UI that allows us to EFFICIENTLY scroll through AIS data

# Downloading the 2024 AIS data (116Gb)


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