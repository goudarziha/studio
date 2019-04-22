import subprocess


def time_symmatry_overlay(video, overlay, fast, slow, output):
    cmd = "ffmpeg -y -i {} -i {} -filter_complex '[0:v]trim=0:3,setpts={}*(PTS-STARTPTS)[fast1];[0:v]trim=3:4,setpts={}*(PTS-STARTPTS)[slow1];[0:v]trim=4:7,setpts={}*(PTS-STARTPTS)[fast2];[0:v]trim=7:8,setpts={}*(PTS-STARTPTS)[slow2];[0:v]trim=8:11,setpts={}*(PTS-STARTPTS)[fast3];[0:v]trim=11:12,setpts={}*(PTS-STARTPTS)[slow3];[fast1][slow1][fast2][slow2][fast3][slow3]concat=n=6:v=1:a=0[out];[out]crop=720:720[crop];[crop]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2[final]' -map '[final]' -crf 18 -preset medium {}".format(
        video, overlay, float(fast), float(slow), float(fast), float(slow), float(fast), float(slow), output)
    subprocess.call(cmd, shell=True)
