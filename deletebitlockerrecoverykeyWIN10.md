How to delete the Bitlocker recovery key with Windows 10.


1. Visit onedrive.live.come to go to the BitLocker recovery keys page on your online Microsoft account OneDrive page and sign in if not already.

2. Click the computer name or Removable data drives – BitLocker To Go where the recovery keys were saved from to see them.

3. Click the Delete link to the right of the recovery key you want to remove from your OneDrive.

4. If you delete all saved recovery keys from a computer, the computer name will also be removed.

5. Click Delete on the prompt to confirm.

https://www.thewindowsclub.com/delete-bitlocker-recovery-key-from-onedrive-in-windows-10


Script to do this:

$TpmProtectorID = ((Get-BitLockerVolume -MountPoint c).KeyProtector | Where-Object KeyProtectorType -EQ 'Tpm').KeyProtectorID

Remove-BitLockerKeyProtector -MountPoint c -KeyProtectorId $TpmProtectorID
Restart-Computer -Force
