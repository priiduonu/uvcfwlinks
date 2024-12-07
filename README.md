# uvcfwlinks

Sometimes you may need to upgrade or downgrade a standalone UniFi Protect
device (not adopted by UniFi Cloud Key or NVR).

`uvcfwlinks` is a script for fetching the firmware download links for the UVC
cameras.

## usage

```
./uvcfwlinks.py -h
usage: uvcfwlinks.py [-h] [-p PLATFORM]

Fetch firmware information from the Ubiquiti firmware API.

options:
  -h, --help            show this help message and exit
  -p PLATFORM, --platform PLATFORM
                        return all f/w info for the given platform
```

It lists the latest versions for all camera platforms when executed without
any options.

When executed with the `--platform` option, it lists all available versions
for the specified platform.

There are different versions of the firmware, depending of the platform used
by the device model:

| platform | model(s)                                                                              |
|----------|---------------------------------------------------------------------------------------|
| a5s      | UVC Bullet, UVC Dome, UVC Micro, UVC Pro                                              |
| cv22     | AI DSLR                                                                               |
| cv2x     | AI 360, AI Bullet, AI Pro, AI Theta                                                   |
| s2l      | G3 Bullet, G3 Dome, G3 Flex, G3 Pro                                                   |
| s2lb     | Vision Go                                                                             |
| s2lm     | Vision Go, G3 Micro                                                                   |
| s5l      | G4 Bullet, G4 Dome, G4 Doorbell, G4 Doorbell Pro, G4 Doorbell Pro PoE, G4 Pro, G4 PTZ |
| sav500db | ???                                                                                   |
| sav530q  | G4 Instant, G5 Bullet, G5 Dome, G5 Flex, G5 Pro, G5 PTZ, G5 Turret Ultra              |
| sav532q  | G3 Instant                                                                            |
| sav837gw | G4 Instant, G5 Bullet, G5 Dome, G5 Flex, G5 Pro, G5 PTZ, G5 Turret Ultra              |

This information has been gathered from
<https://www.reddit.com/r/Ubiquiti/comments/1dp3x1g/unifi_protect_camera_platform_codes_to_actual/>

> [!WARNING]
> Do not try to upload a firmware built for another platform to your device!

> [!TIP]
> You are welcome to contribute to this information by creating a new issue or
  pull request.
