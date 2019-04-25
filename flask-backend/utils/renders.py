import subprocess

# clippp


def time_symmatry_overlay(video, overlay, fast, slow, output):
    cmd = "ffmpeg -y -i {} -i {} -filter_complex '[0:v]trim=0:3,setpts={}*(PTS-STARTPTS)[fast1];[0:v]trim=3:4,setpts={}*(PTS-STARTPTS)[slow1];[0:v]trim=4:7,setpts={}*(PTS-STARTPTS)[fast2];[0:v]trim=7:8,setpts={}*(PTS-STARTPTS)[slow2];[0:v]trim=8:11,setpts={}*(PTS-STARTPTS)[fast3];[0:v]trim=11:12,setpts={}*(PTS-STARTPTS)[slow3];[fast1][slow1][fast2][slow2][fast3][slow3]concat=n=6:v=1:a=0[out];[out]crop=720:720[crop];[crop]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2[final]' -map '[final]' -crf 18 -preset medium {}".format(
        video, overlay, float(fast), float(slow), float(fast), float(slow), float(fast), float(slow), output)
    subprocess.call(cmd, shell=True)

# Simple 5 cuts with reverse


def studio(input_video, overlay, reverse_speed, output):
    cmd = "ffmpeg -y -i {} -i {} -filter_complex '[0:v]trim=0:2,setpts=PTS-STARTPTS[cut1];[0:v]trim=0:2,setpts={}*PTS-STARTPTS,reverse[reverse1];[0:v]trim=3:5,setpts=PTS-STARTPTS[cut2];[0:v]trim=3:5,setpts={}*PTS-STARTPTS,reverse[reverse2];[0:v]trim=5:7,setpts=PTS-STARTPTS[cut3];[0:v]trim=5:7,setpts={}*PTS-STARTPTS,reverse[reverse3];[0:v]trim=7:9,setpts=PTS-STARTPTS[cut4];[0:v]trim=7:9,setpts={}*PTS-STARTPTS,reverse[reverse4];[0:v]trim=9:11,setpts=PTS-STARTPTS[cut5];[0:v]trim=9:11,setpts={}*PTS-STARTPTS,reverse[reverse5];[cut1][reverse1][cut2][reverse2][cut3][reverse3][cut4][reverse4][cut5][reverse5]concat=n=10:v=1:a=0,crop=720:720,overlay[final]' -map '[final]' -crf 18 -r 24 -preset medium {}".format(
        input_video, overlay, reverse_speed, reverse_speed, reverse_speed, reverse_speed, reverse_speed, output)
    return cmd
