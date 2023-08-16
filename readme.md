
# m4a_audiotrimmer

A simple command-line utility to trim `.m4a` audio files based on specified timestamps.

## Requirements

- `ffmpeg`: This tool relies on the powerful multimedia framework `ffmpeg`. Ensure it's installed and accessible in your system's path. [Download ffmpeg here](https://ffmpeg.org/download.html).

## Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/m4a_audiotrimmer.git
cd m4a_audiotrimmer
```

2. Ensure you have `ffmpeg` installed on your system. You can check its availability using:
```bash
ffmpeg -version
```

## Usage

Use the script with the following syntax:
```bash
python trim_m4a.py <path_to_input.m4a> hh:mm:ss-hh:mm:ss <path_to_output.m4a>
```

**Example:** 

To trim the file `input.m4a` from 00:01:00 to 00:02:00 and save it as `output.m4a`, run:
```bash
python trim_m4a.py input.m4a 00:01:00-00:02:00 output.m4a
```

## Contributions

Feel free to fork this project, open issues, or submit pull requests. Any contributions are welcome!

## License

MIT License. See [LICENSE](./LICENSE) for more details.
