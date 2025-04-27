import subprocess
import platform

def run_ps(command):
    try:
        ps_command = f"powershell -command \"{command}\""
        result = subprocess.check_output(ps_command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Erreur PowerShell : {e}"

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}\n")

def get_system_info():
    return run_ps("(Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version)")

def get_cpu_info():
    return run_ps("Get-CimInstance Win32_Processor | Select-Object Name, LoadPercentage, MaxClockSpeed")

def get_ram_info():
    command = (
        'powershell -command "$os = Get-CimInstance Win32_OperatingSystem; '
        '$total = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2); '
        '$free = [math]::Round($os.FreePhysicalMemory / 1MB, 2); '
        'Write-Output \\"RAM Totale : $total Go`nRAM Libre : $free Go\\" "'
    )
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except Exception as e:
        return f"Erreur RAM : {e}"

def get_disks_info():
    command = (
        'powershell -command "Get-PSDrive -PSProvider FileSystem | '
        'Select-Object Name, @{Name=\'LibreGo\';Expression={[math]::Round($_.Free/1GB,2)}}, '
        '@{Name=\'TotalGo\';Expression={[math]::Round(($_.Used+$_.Free)/1GB,2)}}"'
    )
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except Exception as e:
        return f"Erreur disque : {e}"

def get_top_processes():
    return run_ps("""
    Get-Process | Sort-Object CPU -Descending | 
    Select-Object -First 5 Name, ID, CPU, WorkingSet
    """)

def get_network_info():
    return run_ps("Get-NetIPAddress | Where-Object { $_.AddressFamily -eq 'IPv4' -and $_.PrefixOrigin -ne 'WellKnown' } | Select-Object InterfaceAlias, IPAddress")

def main():
    if platform.system() != "Windows":
        print("Ce script est conçu pour Windows uniquement.")
        return

    print_section("INFOS SYSTÈME")
    print(get_system_info())

    print_section("CPU")
    print(get_cpu_info())

    print_section("RAM")
    print(get_ram_info())

    print_section("DISQUES")
    print(get_disks_info())

    print_section("TOP PROCESSUS")
    print(get_top_processes())

    print_section("RÉSEAU")
    print(get_network_info())

if __name__ == "__main__":
    main()