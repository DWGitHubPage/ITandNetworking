$vmsToCheck = "get-content c:\scripts\vmdata.txt"
foreach ($vm in $vmsToCheck) {
 
    get-vm $vm | select vmname, vmhost, NumCPU, RAM | export-csv "c:\data\result.csv"
}