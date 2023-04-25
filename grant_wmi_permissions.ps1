# Grant_WMI_Permissions.ps1

$namespace = "root\cimv2"
$user = "$env:USERDOMAIN\$env:USERNAME"
$permission = 0x1 # Remote Enable

$security_descriptor = (Get-WmiObject -Class __SystemSecurity -Namespace $namespace -List).GetSecurityDescriptor().Descriptor
$trustee = ([wmiclass]"Win32_Trustee").CreateInstance()
$trustee.Domain = $env:USERDOMAIN
$trustee.Name = $env:USERNAME

$ace = ([wmiclass]"Win32_Ace").CreateInstance()
$ace.AccessMask = $permission
$ace.AceType = 0 # Access Allowed
$ace.Trustee = $trustee

$security_descriptor.DACL += @($ace)

Set-WmiInstance -Class __SystemSecurity -Namespace $namespace -Argument @{SD = $security_descriptor} | Out-Null
