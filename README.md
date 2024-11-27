![Python Version](https://img.shields.io/badge/python-3.8.18-blue) 
![Numpy Version](https://img.shields.io/badge/numpy-1.24.4-orange) 
![OpenCV Version](https://img.shields.io/badge/opencv--contrib--python-4.10.0.84-brightgreen)

# Video Processing Scripts

This project contains two Python scripts: `extract_frames.py` and `extract_faces.py`. These scripts allow you to extract frames and faces from a video file with customizable options.

## Prerequisites

Install the required Python dependencies using:

```bash
pip install -r requirements.txt
```

## Quick Start

1. **Place your video file** named `target.mp4` in the same directory as the scripts.
2. **Run the scripts** using the commands below. By default, the scripts use `target.mp4` and save results in the `output/` folder.

### Extract Frames from Video

Extract frames at 1 frame per second (default) and save them to `output/frames`:

```bash
python extract_frames.py
```

### Extract Faces from Video

Extract faces using face detection and save square images resized to 256x256 pixels (default) in `output/faces`:

```bash
python extract_faces.py
```

---

## Customization Options

Both scripts support the following customizable parameters. You can specify them via command-line arguments:

### `extract_frames.py` Parameters

| Argument         | Description                           | Default Value    |
|-------------------|---------------------------------------|------------------|
| `--video_path`    | Path to the video file               | `target.mp4`     |
| `--output_folder` | Folder to save extracted frames      | `output/frames`  |
| `--fps`           | Frames per second to extract         | `1`              |

#### Example

Extract frames from a custom video with 2 FPS:

```bash
python extract_frames.py --video_path example.mp4 --fps 2
```

---

### `extract_faces.py` Parameters

| Argument          | Description                            | Default Value    |
|--------------------|----------------------------------------|------------------|
| `--video_path`     | Path to the video file                | `target.mp4`     |
| `--output_folder`  | Folder to save extracted face images  | `output/faces`   |
| `--image_size`     | Size of the square output face images | `256` (pixels)   |
| `--fps`            | Frames per second to process          | `1`              |

#### Example

Extract faces resized to 500x500 pixels:

```bash
python extract_faces.py --image_size 500
```

---

## Key Features

- **Quick Use**: Simply place your `target.mp4` file in the same directory and run the scripts without parameters.
- **Customizable**: Adjust FPS, output folders, and image sizes as needed.
- **Output Structure**: Frames and faces are saved separately in organized directories (`output/frames` and `output/faces`).

For detailed usage, refer to the README and customize as per your project needs!