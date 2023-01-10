# video2jpg

The method `convert_video2jpg` converts a video into *JPEG* images using *FFmpeg*.

Required parameters are:

*   Video file
*   Frames per second (FPS)
*   Output filename format

For example

```bash
convert_video2jpg "foobar.mp4" 30 "img_%08d.jpg"
```

will result in the following output files:

```
img_00000001.jpg
img_00000002.jpg
img_00000003.jpg
img_00000004.jpg
img_00000005.jpg
img_00000006.jpg
```
