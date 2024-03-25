# Environment Display for Raspberry Pi with Sense Hat

This script was written for a Raspberry Pi 4 with a Sense Hat in a C4Labs Zebra case.

## Install

The service file should be installed to `~/.config/systemd/user/environment_stats.service`.

```bash
mkdir -p ~/.config/systemd/user
cp ./environment_stats.service ~/.config/systemd/user/environment_stats.service
```

Ensure the script is executable:

```bash
chmod +x ./env_report.py
```

Enable the service:

```bash
systemctl --user enable environment_stats.service
```

Start the service:

```bash
systemctl --user start environment_stats.service
```

## Restarting, Stopping, Disabling

Restart:

```bash
systemctl --user restart environment_stats.service
```

Stop:

```bash
systemctl --user stop environment_stats.service
```

Disable:

```bash
systemctl --user disable environment_stats.service
```
