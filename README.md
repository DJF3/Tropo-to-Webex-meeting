# Tropo to Webex Meeting


## What it does
1. The script calls the phone number of someone that needs to be in a Webex meeting.
2. This person is asked "do you want to attend?" and can say the answer (yes/no).
3. If yes, the attendee is transferred to a Webex dial-in number and the meeting ID is entered for them. 


## Use-case
This can be useful in emergency scenarios. What if you need people to be in a meeting **_REALLY FAST_**. 
You could send them an email or a message, but _nothing arrives faster than a voice-call_.
The user would _only_ have to pick-up their phone and say yes or no


## Install
- Edit the script to have the Webex audio dial in number of your choice. ([list here](http://www.cisco.com/c/en/us/about/conferencing-global-access-numbers.html)) - check the 'NOTE' section on this page!
- Create a tropo application and add a phone number to it that has outgoing calls activated. (you may have to contact Tropo support if you don't have this). 
- Paste the code in this repository in the Tropo application
- Save
- Get Application token URL (click 'show URL' at bottom of your Tropo application screen)
- to this URL, append
```
 &yourphone=**YOUR_PHONE_NR**&yourmeetingid=**MEETING_TO_JOIN**
```
- Of course you have to get a valid Webex meeting ID. This _could_ also be a Webex Personal Room meeting ID (which is fixed)
- **NOTE**: The meeting has to be active in order to join the meeting. 
- Launch the URL


## Requirements
- a (free) Tropo developer account on [Tropo.com](https://www.tropo.com/) or [Tropo.eu](https://www.tropo.eu/)
- [Webex](https://www.webex.com) account 


## NOTE
- Tip: (untested) You could also test by calling a SIP URI instead of a phone number (easier/cheaper to test?)
- Tip: replace the Music On Hold music with a spoken message asking the user to check their email for a Webex meeting invitation.
- Tip: you could create a 'master' script that uses [Webex API's](http://www.webexdeveloper.com) to create the meeting. It could then launch this script a number of times based on the required attendees. 


### Webex Dial-in DTMF
The current DTMF sequence is based on the one used by the Webex Amsterdam dial-in number: 
``` 
postd=pp"+str(yourmeetingid)+"#pp#;
```
Which equals: wait 2x 2 seconds + send meeting id + send # + wait 2x 2 seconds + send #
Result: Webex answers, wait 4 seconds, send meeting ID + '#', wait 4 seconds, press '#' to join the meeting.

If your Webex dial-in starts with a language question the script would probably look like this:
``` 
postd=pp**1p**"+str(yourmeetingid)+"#pp#;
```
right after the first 'pp' I added "1p" ==> answer 1 to the language question and wait 2 seconds before entering the meeting ID.

Depending on the Webex dial-in number this sequence could be slightly different. Test it out first. 
If you want to change the DTMF, check out the [Tropo Transfer() method](https://www.tropo.com/docs/scripting/transfer) documentation (search for 'postd'). 
