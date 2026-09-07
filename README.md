# SDCodex-GalleryDL

SDCodex Plugin for automated Gallery-DL tasks, single downloads, Kiosks, and OAuth credential management.

## Features
- **Tasks**: Scheduled and automated batch image downloads via `gallery-dl` and `yt-dlp`.
- **Quick Download**: Single URL rapid fetching with real-time log streaming.
- **Kiosks**: Slideshow displays for local images and collections.
- **OAuth**: Securely authorize platforms such as Reddit, DeviantArt, Flickr, and Tumblr.
- **Config**: In-browser gallery-dl configuration editor and backup/restore.

## Required Volumes (Docker)
- `TASKS`: Host path for tasks directory (defaults to `./tasks`).
- `CONFIG`: Host path for configuration directory (defaults to `./config`).
- `IMAGES`: Host path for downloads output directory (defaults to `./downloads`).

## Installation
Add this repository (`DeeplabSystems/SDCodex-GalleryDL`) in SDCodex Settings -> Plugins.
