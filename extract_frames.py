import cv2
import os
import argparse

def extract_frames(video_path='target.mp4', output_folder='output/frames', fps=1):
    """
    從影片中提取幀並保存為圖片。

    :param video_path: 影片的檔案路徑
    :param output_folder: 圖片保存的資料夾
    :param fps: 提取的幀頻率（每秒提取多少幀）
    """
    # 打開影片檔案
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # 設置影片的幀數
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps == 0:
        print("Error: Video FPS is 0, unable to process the video.")
        cap.release()
        return

    # 確保我們每秒提取固定幾個幀
    frame_interval = int(video_fps // fps)  # 用整數除法來計算間隔

    # 用來計算應該保存的幀
    frame_count = 0
    saved_count = 0
    
    # 創建輸出資料夾
    os.makedirs(output_folder, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 只選擇指定的幀
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1
    
    cap.release()
    print(f"Extracted {saved_count} frames to {output_folder}")

if __name__ == "__main__":
    # 設定命令行參數
    parser = argparse.ArgumentParser(description='Extract frames from a video.')
    parser.add_argument('video_path', type=str, nargs='?', default='target.mp4', help='Path to the video file')
    parser.add_argument('--output_folder', type=str, default='output/frames', help='Folder to save extracted frames')
    parser.add_argument('--fps', type=int, default=1, help='Frames per second to extract')
    
    # 解析命令行參數
    args = parser.parse_args()

    # 執行函數
    extract_frames(args.video_path, args.output_folder, args.fps)