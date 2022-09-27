Cisco Discovery Protocol commands:

If there is a CDP attack and you need to disable CDP:<br>
no cdp enable

To renable CDP globablly:
cdp run

To renable CDP on a specific interface:
cdp enable

To display global CDP information, including timer and hold-time information, use the show cdp command in privileged EXEC mode.:<br>
show cdp

Example:
Router# show cdp

To display information about a specific neighboring device discovered using CDP, use the show cdp entry command in privileged EXEC mode:<br>
show cdp entry {* | entry-name [protocol | version]}


[CDP Command Reference](https://www.cisco.com/c/en/us/td/docs/optical/cpt/r9_5/command/reference/cpt95_cr/cpt95_cr_chapter_01101.pdf)
