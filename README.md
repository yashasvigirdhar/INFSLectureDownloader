# INFSLectureDownloader

## Objective
Download and access [INFS diploma][1] lectures offline when there's no internet connection.

## Background
INFS website uses [embedded vimeo video player][2]. The video content is domain restricted so we can't access it directly on the vimeo website even if we know the `video id`. The player uses HLS `m3u8` playlist to play the video (see below for more details).

## Downloading the video

### Find the .m3u8 Playlist URL
1. Open DevTools (F12) → Network tab
2. Start playing the embedded Vimeo video
3. Filter by .m3u8 or "Media"
4. Look for a URL like:

> https://vod-adaptive.vimeocdn.com/.../playlist.m3u8?exp=...&hmac=...

Once you have the url, you can use any of the below two methods:

### Using yt-dlp [Recommended]

[yt-dlp][3] Supports downloading the whole video given a `m3u8` playlist url. This is much faster as it downloads segments in parallel.

Usage: ```yt-dlp "<m3u8_url>"```

### Directly using ffmpeg

We can pass the `m3u8` playlist url directly to ffmpeg. See `downloader.py` script in this repo which is a small wrapper over it.

Usage: ```python downloader.py``` . The script will then interactively ask for the playlist url.

## More Information about HLS

### HLS = HTTP Live Streaming

- HLS is a media streaming protocol developed by Apple.
- It streams video as **many small segments** instead of one large file.
- These segments are listed in a playlist file with the `.m3u8` extension.
- The video player fetches and plays segments one by one, adapting quality based on network speed.

---

### 📄 Types of HLS Playlists

1. **Master Playlist (`.m3u8`)**
   - Lists all available video qualities (1080p, 720p, 480p, etc.)
   - Each quality points to its own media playlist

2. **Media Playlist**
   - Lists actual video segments, e.g.:
     ```
     #EXTINF:6.0,
     segment0001.ts
     #EXTINF:6.0,
     segment0002.ts
     ```

---

### 🎥 Why Vimeo Uses HLS

- ✅ **Adaptive Streaming** — Matches video quality to user bandwidth
- ✅ **Separation of Audio/Video** — More efficient encoding and reuse
- ✅ **CDN-Friendly** — Small chunks are cacheable and resilient
- ✅ **Security** — Expiring, signed URLs prevent hotlinking
- ✅ **Domain Restrictions** — Only allow playback on approved domains

---

### 🔐 Example of a Secure Vimeo `.m3u8` URL

> https://vod-adaptive-ak.vimeocdn.com/exp=1746182572~acl=%2F319911d5-a613-4a35-b46b-4104276930a0%2F%2A~hmac=6b72f94365b2cfa402e87b86308aa74293e4b8541a8bc46fb08fc20163c69edf/319911d5-a613-4a35-b46b-4104276930a0/v2/playlist/av/primary/sub/124444657-c-en-x-autogen/prot/cXNyPTE/playlist.m3u8?ext-subs=1&locale=en&omit=opus&pathsig=8c953e4f~Ns9F6tGfNwDEFtzBGHcvfj6xkxGckQ9KcFj_h2aUGyM&qsr=1&r=dXM%3D&rh=2LSs0P&sf=fmp4

- `exp=` - expiration time
- `hmac=` - signature hash
- `pathsig=` - path validation
- These make the playlist temporary and secure.

---

### 🔁 How Playback Works

1. Vimeo's player requests the `.m3u8` master playlist.
2. The browser chooses the best stream based on bandwidth.
3. It downloads and buffers segment-by-segment.
4. Playback continues until all segments are fetched.





[1]: https://www.infs.com/course/DiplomaInNutritionAndFitness-82
[2]: https://annotely.com/preview/acma6g6auh000103ldcx4ob1eq
[3]: https://github.com/yt-dlp/yt-dlp
