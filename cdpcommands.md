Cisco Discovery Protocol commands:
______________________________________________________________________________________________

If there is a CDP attack and you need to disable CDP:<br>
no cdp enable
______________________________________________________________________________________________
To renable CDP globabally:<br>
cdp run
______________________________________________________________________________________________
To renable CDP on a specific interface:<br>
cdp enable
______________________________________________________________________________________________
To display global CDP information, including timer and hold-time information, use the show cdp command in privileged EXEC mode.:<br>
show cdp

Example:<br>
Router# show cdp
______________________________________________________________________________________________
To display information about a specific neighboring device discovered using CDP, use the show cdp entry command in privileged EXEC mode:<br>
show cdp entry {* | entry-name [protocol | version]}
______________________________________________________________________________________________

To display information about traffic between devices gathered using CDP, use the show cdp traffic command in privileged EXEC mode:<br>
show cdp traffic

* This command has no arguments or keywords

______________________________________________________________________________________________
[CDP Command Reference](https://www.cisco.com/c/en/us/td/docs/optical/cpt/r9_5/command/reference/cpt95_cr/cpt95_cr_chapter_01101.pdf)
