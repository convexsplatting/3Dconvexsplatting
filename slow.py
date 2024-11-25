from moviepy.editor import VideoFileClip, vfx

def slow_down_video(input_path, output_path, slowdown_factor):
    """
    Slows down an MP4 video by a given factor.
    
    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the slowed-down video.
        slowdown_factor (float): Factor by which to slow down the video (e.g., 2.0 for half-speed).
    """
    try:
        # Load the video
        clip = VideoFileClip(input_path)
        
        # Apply the slowdown factor
        slowed_clip = clip.fx(vfx.speedx, factor=1.0 / slowdown_factor)
        
        # Write the result to a new file
        slowed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Video has been slowed down and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_video = "C:/Users/Jan Held/Downloads/render_traj_color_10.mp4"
output_video = "truck_10.mp4"  # Path to save the slowed video
slowdown_factor = 4.0  # Slowdown factor (2.0 means the video will play at half speed)

slow_down_video(input_video, output_video, slowdown_factor)
