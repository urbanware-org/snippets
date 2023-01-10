video2jpg() {
    input_video_file="$1"
    input_video_fps="$2"
    output_filename="$3"
    
    if [ -z "$input_video_fps" ]; then
        input_video_fps=30
    fi
    if [ -z "$output_filename" ]; then
        output_filename="img_%08d.jpg"
    fi

    ffmpeg -i "$input_video_file" -vf fps=$input_video_fps "$output_filename"
}
