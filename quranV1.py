import os
import subprocess
import sys
import time
import threading
from itertools import cycle

# إعداد المسارات
BASE_DIR = os.getcwd()
BG_DIR = os.path.join(BASE_DIR, "quran_backgrounds")
CHROMA_DIR = os.path.join(BASE_DIR, "quran_chroma")
OUTPUT_DIR = os.path.join(BASE_DIR, "quran_output")

# إنشاء المجلدات
for d in [BG_DIR, CHROMA_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    # بانر احترافي بمسافات مظبوطة تماماً
    banner = r"""
    [92m
     ██████╗ ██╗   ██╗██████╗  █████╗ ███╗   ██╗
    ██╔═══██╗██║   ██║██╔══██╗██╔══██╗████╗  ██║
    ██║   ██║██║   ██║██████╔╝███████║██╔██╗ ██║
    ██║▄▄ ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║
    ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚████║
     ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    [94m        --- QURAN GHOST PRO - Developed by BODA ---
    [0m"""
    print(banner)

def loading_spinner(stop_event, message):
    spinner = cycle(['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘'])
    while not stop_event.is_set():
        sys.stdout.write(f'\r[93m[{next(spinner)}] {message}...[0m')
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write('\r' + ' ' * (len(message) + 15) + '\r')

def create_quran_video(bg_name, chroma_name):
    bg_path = os.path.join(BG_DIR, bg_name)
    chroma_path = os.path.join(CHROMA_DIR, chroma_name)
    output_name = f"final_{chroma_name.replace(' ', '_')}"
    output_path = os.path.join(OUTPUT_DIR, output_name)

    print(f"[96m[📁] Target File:[0m {chroma_name}")

    filter_complex = (
        f"color=c=black:s=1080x1920:d=5[black];" 
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,format=rgba,colorchannelmixer=aa=0.45[bg_trans];"
        f"[black][bg_trans]overlay=shortest=1[base];"
        f"[1:v]scale=1080:1920:force_original_aspect_ratio=decrease,colorkey=0x000000:0.1:0.1[txt];"
        f"[base][txt]overlay=(W-w)/2:(H-h)/2[v]"
    )

    cmd = [
        'ffmpeg', '-i', bg_path, '-i', chroma_path,
        '-filter_complex', filter_complex,
        '-map', '[v]', '-map', '1:a?', 
        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '22',
        '-c:a', 'aac', '-b:a', '192k', '-shortest',
        output_path, '-y'
    ]

    stop_event = threading.Event()
    loader = threading.Thread(target=loading_spinner, args=(stop_event, "Rendering Ghost Video"))
    loader.start()

    try:
        process = subprocess.run(cmd, capture_output=True, text=True)
        stop_event.set()
        loader.join()

        if process.returncode == 0:
            print(f"[92m[✅] SUCCESS:[0m {output_name} saved!\n")
        else:
            # طباعة الخطأ لو حصل لمساعدتك في التصحيح
            print(f"[91m[❌] FFMPEG ERROR:[0m {process.stderr[-100:]}\n")
    except Exception as e:
        stop_event.set()
        print(f"\n[91m[❌] CRITICAL ERROR: {e}[0m")

if __name__ == "__main__":
    clear_screen()
    show_banner()

    bgs = [f for f in os.listdir(BG_DIR) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]
    chromas = [f for f in os.listdir(CHROMA_DIR) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]

    if not bgs or not chromas:
        print("[91m⚠️  Required files missing in folders![0m")
        sys.exit()

    print(f"[95m[🚀] Processing {len(chromas)} videos...[0m")
    print("━" * 45)

    for i, chroma in enumerate(chromas):
        current_bg = bgs[i % len(bgs)]
        create_quran_video(current_bg, chroma)

    print("━" * 45)
    print(f"[92m⭐ MISSION COMPLETE - FOLLOW BODA FOR MORE TOOLS[0m")
  
