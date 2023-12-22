# video2jpg

The function `convert_video2jpg` converts a video into *JPEG* images using *FFmpeg*.

Required parameters are:

*   Input video file
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

Even though, the function is called `video2jpg` the frames can also be saved in the *PNG* image format:

```bash
convert_video2jpg "foobar.mp4" 30 "img_%08d.png"
```

However, the output filename format must be explicitly given as in the example above. Otherwise the default format `img_%08d.jpg` will be used.
