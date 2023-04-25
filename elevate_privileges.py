import os
import sys
import ctypes
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Ensure the script has admin privileges and WMI permissions are granted
def elevate_privileges_and_grant_wmi_permissions(script_path):
    if not is_admin():
        # Re-run the script with administrator privileges and wait for it to finish
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"\"{os.path.abspath(script_path)}\"", None, 1)
        if hinstance <= 32:
            raise RuntimeError("Failed to run the script with administrator privileges.")
        sys.exit()

    # Execute the PowerShell script to grant WMI permissions as administrator
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ps_script = os.path.join(script_dir, "grant_wmi_permissions.ps1")
    try:
        subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script], check=True)
    except subprocess.CalledProcessError as e:
        if "cannot be loaded because running scripts is disabled on this system" in str(e):
            # PowerShell script execution is blocked. Change the execution policy to allow scripts to run.
            subprocess.run(["powershell.exe", "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"], check=True)
            # Retry running the PowerShell script
            subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script], check=True)
