## Unbounce I.T. Machine Uptime Nag

This script checks the current uptime of the computer and posts a notification via [Yo][1]. This repo is built as a [munki-pkg][2] project ready to be packaged for deployment. 

### How it works
There are two elements to this program. The first is `check_uptime.py` which gets installed at `/usr/local/uptime_nag`. This script checks the epoch time of the last boot and subtracts that from current epoch time. If that time is over 30 days it uses `subproces` to call the Yo CLI (`yo_scheduler`) alerting the user that they need to reboot their computer. Because of the character limit in Apple macOS Notification popups the Yo notification can additionally trigger an AppleScript that can provide more info. The second element is a `launchd` LaunchAgent that runs the script every 2 hours i.e. if the user IS over 30 days and ignores the first notification they'll get another in two hours. 

### Packaging the application
The repo is built around a `munki-pkg` repo. Make sure thats installed and in your `$PATH`. Use the `build-info.yaml` file to edit the properties of the build package. Make sure its signed for christs sake. 

### Troubleshooting 
The launchd outputs errors and stdout to `/ApplicationSupport/UptimeNag`. 

[1]: https://github.com/sheagcraig/yo
[2]: https://github.com/munki/munki-pkg
