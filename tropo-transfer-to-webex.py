# ------- Transfer caller to Webex meeting + enter meeting ID ---------
#      DJ Uittenbogaard  https://github.com/DJF3/Tropo-to-Webex-meeting
# ---------------------------------------------------------------------

myWebexAudioDN = "+31203571487"

# Call the attendee phone
call(yourphone, {"timeout":120})
wait(1000)

# Ask if user wants to join the meeting
result = ask("Hello, there is an emergency meeting. Want to join? Say yes or no.", {
    "voice":"Daniel",
    "choices":"yes, no",
    "timeout":10.0})
# Confirm the choice
say("You said " + result.value)

# If choice was 'yes' then forward call and send meeting ID digits
if (result.value == "yes") :
    say("I will transfer you to the meeting", {"voice":"Karen"})
    transfer(myWebexAudioDN + ";postd=pp"+str(yourmeetingid)+"#pp#;pause=2s", {
        "playvalue":"http://www.phono.com/audio/holdmusic.mp3",
        "terminator": "*",
        "timeout":"60.0",
        "onTimeout": lambda event : say("Sorry, but nobody answered.", {"voice":"Karen"})})
else :
    say("you did not say yes, hanging up the call")
