import subprocess
import sys

def trim_m4a(input_file, timestamp, output_file):
    # Split the timestamp
    start_time, end_time = timestamp.split('-')
    
    # Command to trim the m4a file
    cmd = [
        "ffmpeg", 
        "-i", input_file, 
        "-ss", start_time, 
        "-to", end_time, 
        "-c:a", "copy", 
        output_file
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input.m4a> <hh:mm:ss-hh:mm:ss> <output.m4a>")
        sys.exit(1)

    input_file = sys.argv[1]
    timestamp = sys.argv[2]
    output_file = sys.argv[3]

    trim_m4a(input_file, timestamp, output_file)
