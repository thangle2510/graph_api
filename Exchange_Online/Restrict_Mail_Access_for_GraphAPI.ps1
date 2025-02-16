### Install module
Install-Module ExchangeOnlineManagement

# --- Define Variables ---
$AppId = ""
$GroupName = "GraphAPI-MailboxAccess"

# --- Connect to Exchange Online ---
Write-Host "Connecting to Exchange Online..."
Connect-ExchangeOnline -UserPrincipalName admin@example.com

# --- Check if the Application Access Policy already exists ---
$App = Get-ApplicationAccessPolicy | Where-Object {$_.AppId -like $AppId}
$ExistingPolicy = Get-ApplicationAccessPolicy -Identity $App.Identity -ErrorAction SilentlyContinue
if (-not $ExistingPolicy) {
    Write-Host "Creating Application Access Policy to restrict mailbox access..."
    New-ApplicationAccessPolicy -AppId $AppId -PolicyScopeGroupId $GroupName -AccessRight RestrictAccess -Description "Restrict Graph API Mail Access"
} else {
    Write-Host "Application Access Policy already exists. Skipping creation."
}

# --- Verify Policy ---
Write-Host "Verifying Application Access Policy..."
$App = Get-ApplicationAccessPolicy | Where-Object {$_.AppId -like $AppId}
Get-ApplicationAccessPolicy -Identity $App.Identity

Write-Host "Setup Complete! Only specified users' mailboxes can be accessed by the Graph API App."

# --- Disconnect from Exchange Online ---
Disconnect-ExchangeOnline -Confirm:$false

# --- Remove the Policy ---
# $App = Get-ApplicationAccessPolicy | Where-Object {$_.AppId -like $AppId}
# Remove-ApplicationAccessPolicy -Identity $App.Identity
