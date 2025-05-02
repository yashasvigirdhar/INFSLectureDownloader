import subprocess

# Ask the user for the playlist URL
m3u8_url = input("🔗 Paste the Vimeo .m3u8 playlist URL: ").strip()

# Optional: You can validate if it looks like a valid URL here
if not m3u8_url.startswith("http"):
    print("❌ Invalid URL. Please make sure it starts with http or https.")
    exit(1)

output_file = "output.mp4"

# Run ffmpeg to download and merge the video
print(f"📥 Downloading and merging video from:\n{m3u8_url}\n")

try:
    subprocess.run([
        'ffmpeg', '-y',
        '-i', m3u8_url,
        '-c', 'copy',
        '-bsf:a', 'aac_adtstoasc',
        output_file
    ], check=True)
    print(f"✅ Download complete. Saved as {output_file}")
except subprocess.CalledProcessError:
    print("❌ ffmpeg failed. Please check the URL or try again.")
