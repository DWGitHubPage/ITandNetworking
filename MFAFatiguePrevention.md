MFA fatigure (also called prompt bombing) is a cyber attack where 
criminals target a user’s multiple factor authentication app by sending many 
push requests for account access. This technique only works if the threat actor 
already has the credentials of a targeted account from a previous compromise such
as phishing, credential replay, brute forcing, or password spraying. It also relies
on being an annoyance to users which maybe get them to just accept it to get rid of
the notification.


MFA fatigue notifications to be aware of:

1. Unexpected MFA request push notifications.  

2. From an unfamiliar location (If the request is coming in from a country or city 
different from the one, you’re currently in. If you’re using a VPN, be aware of the 
location of where your VPN is routing you out of). 

3. Receiving a call, email or message from someone claiming to be from your IT team performing 
an MFA test and asking you to accept the MFA request notifications that you’re receiving. 

4. A rapid-fire sequence of MFA request notifications.  


# Things you can also do:

1. Limit MFA request push notifications within a certain timeframe if your MFA provider allows this.

2. Disable MFA request push notifications. Most MFA providers allow you to disable this feature.


# Preventing MFA fatigue attacks in Windows where Microsoft 365 users
are especially targeted.

1. Implement Impossible travel detections.

2. Implement advanced authentication features using geography.

3. Enable Azure MFA number matching MFA codes. (See below on how to enable this feature.)

4. Implement Azure AD Identity Protection.

5. Track alerts for new MFA and MDM device enrollments.

6. Collect AzureAD/MFA events in Microsoft Sentinel.

7. Protect against password spray.


# How to Enable Azure MFA number matching:

1. Go to Azure Active Directory -> Security -> Authentication Methods

2. Within the blade Authentication methods click on "'Policies" and select "Microsoft Authenticator".

3. Under Microsoft Authenticator, choose Enable and target all users or selected users. 
It's recommended to start with Select users and configure some test groups. If you select a group so you can 
pilot this change, the configuration will impact the group and not all users.

4. For the Azure AD number matching feature make sure the setting "Require number matching (Preview)" is enabled. 
Microsoft Managed means that the feature will be enabled by default for all tenants after the General availability of the feature.


# AD identity protection protects in the following ways:

* Atypical travel
* Unfamiliar sign-in properties
* Malicious IP address
* Password spray
* Impossible travel
* New country
* Leaked credentials


Sources:
https://jeffreyappel.nl/mfa-prompt-spamming-mfa-fatigue-what-can-you-do-to-prevent-detect-attacks/
https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match
https://www.twosense.ai/blog/can-you-defend-against-mfa-fatigue
https://arcticwolf.com/resources/blog/growing-risk-of-mfa-fatigue-attacks/
https://intersys.co.uk/2022/05/18/what-is-an-mfa-fatigue-attack-and-how-can-i-prevent-it-2-minute-tech-tips-from-intersys/
