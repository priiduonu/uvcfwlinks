# How to (re)enable direct RTSP streaming in standalone G3 camera

If you want to access the RTSP streams directly from the camera (not from the
UniFi Protect) then this guide might help you.

Direct RTSP streaming is enabled by default in standalone G3 cameras up to the
latest f/w version (`4.72.44` as of today).

RTSP streams can be accessed despite the settings are hidden in the camera web
interface of the firmware versions `>=4.69.55`.

## Steps to follow

- connect the camera to the network
- if the camera has been managed by Protect, you should remove it from
  Protect ("Settings > Remove")

> [!WARNING]
> Wait for the optional upgrade procedure to finish before attempting to
  remove the camera from Protect!

- reset the camera to the factory settings

> [!TIP]
> Refer to <https://help.ui.com/hc/en-us/articles/360043360253-UniFi-Recovery-Mode> for instructions)

This will also restore the factory loaded version of the firmware. My G3 Flex
cameras revert to f/w `UVC.v4.2.5.66.M_b72b2b9.180123.1542` after factory
reset.

- login to the camera web interface with the default credentials (`ubnt/ubnt`)
- when the setup wizard starts, select "Standalone" mode
- complete the setup wizard
- upgrade the firmware as needed (see [remarks](#remarks) below)

The streams can now be reached at:

```html
rtsp://<camera>:554/s0
rtsp://<camera>:554/s1
rtsp://<camera>:554/s2
```

> [!TIP]
> By default, no RTSP authorization is needed. You can check the RTSP server
  configuration by establishing a SSH session with the camera and displaying
  the contents of `/var/etc/persistent/ubnt_nvr.conf`.

## Remarks

| **release notes**                                                                                                 | **remarks** |
|-------------------------------------------------------------------------------------------------------------------|-------------|
| [4.66.11](https://community.ui.com/releases/UniFi-Protect-Cameras-4-66-11/237f1c30-7e48-4157-8aef-f7d1751bd6f8)   |             |
| [4.68.17](https://community.ui.com/releases/UniFi-Protect-Cameras-4-68-17/f8713f88-5e5a-430e-a36b-66d19be9ee4b)   |             |
| [4.68.21](https://community.ui.com/releases/UniFi-Protect-Cameras-4-68-21/9b788892-8d02-4a34-b6a3-77d0ccd420e1)   |             |
| [4.69.55](https://community.ui.com/releases/UniFi-Protect-Cameras-4-69-55/4178d90c-7d44-4e63-9023-48ce547dc896)   | [^1]        |
| [4.69.96](https://community.ui.com/releases/UniFi-Protect-Cameras-4-69-96/5be27013-5515-4fff-a8ab-50b750a25c05)   |             |
| [4.70.32](https://community.ui.com/releases/UniFi-Protect-Cameras-4-70-32/0ea65e12-7959-47c0-a6a9-d328d8320f81)   |             |
| [4.70.39](https://community.ui.com/releases/UniFi-Protect-Cameras-4-70-39/0983bde6-7d96-4553-a50c-1f88f16dfd0b)   |             |
| [4.70.91](https://community.ui.com/releases/UniFi-Protect-Cameras-4-70-91/244d446f-ef98-4160-abe2-78a2e0e5140c)   |             |
| [4.71.85](https://community.ui.com/releases/UniFi-Protect-Cameras-4-71-85/cf0322e3-9024-4948-9e1c-875e2e45c10b)   |             |
| [4.71.95](https://community.ui.com/releases/UniFi-Protect-Cameras-4-71-95/3fc98018-cdde-4aca-9b57-19691e3f77c1)   |             |
| [4.71.133](https://community.ui.com/releases/UniFi-Protect-Cameras-4-71-133/7763dc20-d64a-4c6e-ac5f-95ae6a3a8f18) |             |
| [4.71.147](https://community.ui.com/releases/UniFi-Protect-Cameras-4-71-147/33a8cee7-ed2c-4da0-aea8-ed72ee58e57e) |             |
| [4.71.149](https://community.ui.com/releases/UniFi-Protect-Cameras-4-71-149/a424ec41-f8cc-4a09-9eff-29a4e932c1f0) |             |
| [4.72.36](https://community.ui.com/releases/UniFi-Protect-Cameras-4-72-36/56136a20-c9b6-4529-ab2e-8dd4fb053c3c)   |             |
| [4.72.38](https://community.ui.com/releases/UniFi-Protect-Cameras-4-72-38/3597a7b0-f80e-4272-a685-081368067f0e)   | [^2]        |
| [4.72.44](https://community.ui.com/releases/UniFi-Protect-Cameras-4-72-44/ab38fd24-91eb-4a4b-80fe-b9ba408e6e4e)   |             |

[^1]: from this version onward the _Mode_ and _RTSP_ settings are hidden on the web page but RTSP streaming still works!
[^2]: from this version onward the _Overlay_ settings do not survive reboot, no overlay is displayed

