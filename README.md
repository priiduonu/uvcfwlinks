# uvcfwlinks

Sometimes you may need to upgrade or downgrade a standalone UniFi Protect
device (not adopted by UniFi Cloud Key or NVR).

Here are some direct firmware download links, the filenames have been extracted from
the UniFi Cloud Key log files like this:

```
grep downloaded /srv/unifi-protect/logs/updates.downloadRelease.log
```

There are different versions of the firmware, depending of the platform used
by the device model:

| platform | model(s)    |
|----------|-------------|
| s2l      | G3 Flex     |
| s5l      | G4 Doorbell |
| sav530q  | G5 Flex     |

> [!WARNING]
> Do not try to upload a firmware built for another platform to your device!

> [!TIP]
> You are welcome to contribute to this information by creating a new issue or
  pull request.

## s2l

- https://fw-download.ubnt.com/data/uvc/8de0-s2l-4.34.22-54228f2510454a70976eed0923bcceb3.bin
- https://fw-download.ubnt.com/data/uvc/37d4-s2l-4.36.8-7364926d1f82455482c7edd0384b3a7c.bin
- https://fw-download.ubnt.com/data/uvc/400f-s2l-4.38.1-c7caa70049be4d57a8339f9959d5c447.bin
- https://fw-download.ubnt.com/data/uvc/c50c-s2l-4.41.16-bcf8b0e1872741b780e45c3d4114f711.bin
- https://fw-download.ubnt.com/data/uvc/dce0-s2l-4.46.13-12549106d0b5443881903cde44c9aca6.bin
- https://fw-download.ubnt.com/data/uvc/ffc0-s2l-4.46.18-7574d395d07d4896bc753542a8e2da55.bin
- https://fw-download.ubnt.com/data/uvc/529d-s2l-4.48.44-cbdc9f374bd64f6da62cb86c35a121e9.bin
- https://fw-download.ubnt.com/data/uvc/330e-s2l-4.49.5-dd5aec53ef0e4d708cb2580f115f7b46.bin
- https://fw-download.ubnt.com/data/uvc/b8e0-s2l-4.49.8-386b0ba94e4f46778cb122538f7c21ba.bin
- https://fw-download.ubnt.com/data/uvc/d0c2-s2l-4.49.9-76d951c50d50465e8e7c3616417ee687.bin
- https://fw-download.ubnt.com/data/uvc/7028-s2l-4.51.14-5c2f3b75ca034106a7fc2c9a302789f0.bin
- https://fw-download.ubnt.com/data/uvc/6faa-s2l-4.55.5-4f4c50c47c1f4706a299fdf6f5afe7f4.bin
- https://fw-download.ubnt.com/data/uvc/7764-s2l-4.57.31-dc3b28813f5046d0af1e976aa5601f44.bin
- https://fw-download.ubnt.com/data/uvc/2f30-s2l-4.57.35-99fa83836b7548ac9b7b87cb09efd9c9.bin
- https://fw-download.ubnt.com/data/uvc/19c5-s2l-4.57.36-cea5d270e077465daed73658b3a2c682.bin
- https://fw-download.ubnt.com/data/uvc/9a5f-s2l-4.63.22-43760f965dd54451859fd8a2349505ef.bin
- https://fw-download.ubnt.com/data/uvc/e9d0-s2l-4.64.144-5c781fb61fcb4c5991b6426ef67ce85f.bin
- https://fw-download.ubnt.com/data/uvc/aef8-s2l-4.64.150-44b9a1b475574adbb5c3f47b4ebf743e.bin
- https://fw-download.ubnt.com/data/uvc/81e6-s2l-4.69.55-8a935a2f-482f-42a1-a030-21276ea9e406.bin
- https://fw-download.ubnt.com/data/uvc/5805-s2l-4.69.96-ac373b6d-1d71-4d1f-9bba-e679fa4e388f.bin
- https://fw-download.ubnt.com/data/uvc/0da2-s2l-4.70.32-4f018e7e-037f-4288-bbf3-b72238e312e1.bin
- https://fw-download.ubnt.com/data/uvc/26bd-s2l-4.70.39-9fa49b05-2ccb-4602-8b06-8b6791d2cea9.bin
- https://fw-download.ubnt.com/data/uvc/b648-s2l-4.71.85-dd6e74c3-2579-4692-8f8e-95784a4a5120.bin
- https://fw-download.ubnt.com/data/uvc/41e0-s2l-4.71.95-a67199d3-e521-4fe2-8acd-cff0fcfff910.bin
- https://fw-download.ubnt.com/data/uvc/4df8-s2l-4.71.133-362f82ad-9ed9-4b88-8cf1-842272f0b879.bin
- https://fw-download.ubnt.com/data/uvc/e7f4-s2l-4.71.147-f42e5db2-109c-4433-857e-7b1fc53f1851.bin
- https://fw-download.ubnt.com/data/uvc/3482-s2l-4.71.149-8beeb640-2a19-4e3f-b2d3-d3d1c38a5c90.bin
- https://fw-download.ubnt.com/data/uvc/7f5b-s2l-4.72.36-63ce1db9-bdbd-40d7-be03-4baedeeaa06e.bin

## s5l

- https://fw-download.ubnt.com/data/uvc/c2b2-s5l-4.46.13-96b4d41774234ba0b613d5270f3bb877.bin
- https://fw-download.ubnt.com/data/uvc/dc74-s5l-4.46.18-d790a078cd074c9795b190018ce1fc88.bin
- https://fw-download.ubnt.com/data/uvc/191d-s5l-4.48.44-0f7789aa82f64e838cdc3640cd3fa301.bin
- https://fw-download.ubnt.com/data/uvc/122c-s5l-4.49.5-f3eb6cf7c800419993daf27916277899.bin
- https://fw-download.ubnt.com/data/uvc/62d4-s5l-4.49.8-1f68f0a3be994889bd2eae1b2896403e.bin
- https://fw-download.ubnt.com/data/uvc/4732-s5l-4.49.9-1b3a8fe84af14a46aaab4ef50704ba88.bin
- https://fw-download.ubnt.com/data/uvc/8822-s5l-4.51.14-a3871a9038e54848affc4383b21e060d.bin
- https://fw-download.ubnt.com/data/uvc/6a01-s5l-4.55.5-22e4688ab78a48f998c07ceb509a38d9.bin
- https://fw-download.ubnt.com/data/uvc/21ca-s5l-4.57.31-40fa8a7b28c749329ddb7a9823861f7c.bin
- https://fw-download.ubnt.com/data/uvc/a7ce-s5l-4.57.35-602691d8e2284ff1bb968b622d4bb102.bin
- https://fw-download.ubnt.com/data/uvc/175d-s5l-4.57.36-ca6fa2f1ac0f4b288f6db2f5539537c1.bin
- https://fw-download.ubnt.com/data/uvc/f2ad-s5l-4.63.22-33aae7792c344d8db134fc91cbb99290.bin
- https://fw-download.ubnt.com/data/uvc/7e30-s5l-4.64.144-1675cca214ba4b30acf37f68554190fa.bin
- https://fw-download.ubnt.com/data/uvc/4e9e-s5l-4.64.150-bc202d40365944799c1a2aa284cbccd7.bin
- https://fw-download.ubnt.com/data/uvc/e8ef-s5l-4.69.55-d47949e5-e653-4824-8fb2-13ccedcb98b2.bin
- https://fw-download.ubnt.com/data/uvc/b46e-s5l-4.69.96-c399cc9d-aa39-4fbe-8b9d-8a15ce179c60.bin
- https://fw-download.ubnt.com/data/uvc/80fa-s5l-4.70.32-f9b03a96-635e-4d0e-88bf-5b427b7cc1c6.bin
- https://fw-download.ubnt.com/data/uvc/54ca-s5l-4.70.39-bbb5d154-5773-4b14-b18e-9fdbc0ce436b.bin
- https://fw-download.ubnt.com/data/uvc/1058-s5l-4.71.85-df14f1d0-ad1b-48a1-891f-53783f4e76d0.bin
- https://fw-download.ubnt.com/data/uvc/9df1-s5l-4.71.95-13774222-6a40-4337-a912-cfc480c27280.bin
- https://fw-download.ubnt.com/data/uvc/1bb9-s5l-4.71.133-e8132ac7-3984-46de-a50c-42ee38b3a554.bin
- https://fw-download.ubnt.com/data/uvc/d262-s5l-4.71.147-8c720ff7-57d1-437d-9880-7c96d3c3112f.bin
- https://fw-download.ubnt.com/data/uvc/46f7-s5l-4.71.149-40d794b1-a2f9-4249-b333-8c45b58748d2.bin
- https://fw-download.ubnt.com/data/uvc/f075-s5l-4.72.36-e259a401-084c-4c9d-8f21-cb4c3e718c0e.bin

## sav530q

- https://fw-download.ubnt.com/data/uvc/90fe-sav530q-4.57.36-c8baa2ff7f6148759802e78eaccc73f8.bin
- https://fw-download.ubnt.com/data/uvc/982f-sav530q-4.63.22-4b8e3d99ff83483ea53fb79f9664ecc3.bin
- https://fw-download.ubnt.com/data/uvc/ca8d-sav530q-4.64.144-133a05efe9bc4281970dbcd99336d73f.bin
- https://fw-download.ubnt.com/data/uvc/c600-sav530q-4.64.150-0eab7d3bda5644c4a0dd4d7a496c2776.bin
- https://fw-download.ubnt.com/data/uvc/408c-sav530q-4.69.55-0e01220c-0a4b-47c3-9aba-bcd18257878e.bin
- https://fw-download.ubnt.com/data/uvc/3e40-sav530q-4.69.96-19cd8e28-ee1c-44a2-9d2c-0ac809bba520.bin
- https://fw-download.ubnt.com/data/uvc/e0d5-sav530q-4.70.32-3b4053fb-81da-4079-a1c5-02ac6f56492b.bin
- https://fw-download.ubnt.com/data/uvc/cd8b-sav530q-4.70.39-9d6bb7ae-cb37-4c67-a656-ed16d568049b.bin
- https://fw-download.ubnt.com/data/uvc/0703-sav530q-4.70.91-0407bb1e-37a9-4ff3-b8a6-3f8d50e6da15.bin
- https://fw-download.ubnt.com/data/uvc/0562-sav530q-4.71.85-1e5aef34-8f78-4289-a69b-b61298ab2ec6.bin
- https://fw-download.ubnt.com/data/uvc/b5bb-sav530q-4.71.95-3336103e-fadb-4fb8-ba10-e614ec8de0c0.bin
- https://fw-download.ubnt.com/data/uvc/b264-sav530q-4.71.133-bc5782dd-f842-459c-a50e-88c7bda4d253.bin
- https://fw-download.ubnt.com/data/uvc/802c-sav530q-4.71.147-d684e74a-9e7e-4480-ab03-c56b66670ba3.bin
- https://fw-download.ubnt.com/data/uvc/7dbe-sav530q-4.71.149-49e25a59-4d6f-45d0-ab83-6ab53cce8666.bin
- https://fw-download.ubnt.com/data/uvc/a428-sav530q-4.72.36-1ae915ee-2743-4bb0-84a4-237a37a93bde.bin
