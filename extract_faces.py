import cv2
import os
import argparse

# 初始化人臉識別器 (使用 OpenCV 提供的 Haar Cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def extract_faces(video_path='target.mp4', image_size=256, output_folder='output/faces', fps=1):
    """
    從影片中提取人臉並截取正方形圖片。

    :param video_path: 影片的檔案路徑
    :param output_folder: 圖片保存的資料夾
    :param image_size: 截取的正方形圖片尺寸
    :param fps: 每秒處理的幀數 (每秒提取多少幀)
    """
    # 檢查 fps 是否為 0，防止除零錯誤
    if fps <= 0:
        print("Error: fps must be greater than 0")
        return

    # 打開影片檔案
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # 創建輸出資料夾
    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    saved_count = 0

    # 獲取影片的幀率
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps == 0:
        print("Error: Unable to get video FPS.")
        return

    frame_interval = int(video_fps / fps)  # 計算幀間隔

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # 只在幾個幀後進行處理，避免每一幀都進行處理
        if frame_count % frame_interval == 0:
            # 對每一幀進行灰階轉換，來提高人臉識別效能
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 偵測人臉
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # 若未偵測到人臉，跳過此幀
            if len(faces) == 0:
                continue

            # 遍歷所有偵測到的人臉
            for (x, y, w, h) in faces:
                # 計算截取範圍的中心點，並確保它是正方形
                center = (x + w // 2, y + h // 2)
                side_length = max(w, h)  # 正方形的邊長

                # 計算正方形的裁剪範圍，保持邊界不超出圖片範圍
                x1 = max(center[0] - side_length // 2, 0)
                y1 = max(center[1] - side_length // 2, 0)
                x2 = min(center[0] + side_length // 2, frame.shape[1])
                y2 = min(center[1] + side_length // 2, frame.shape[0])

                # 截取正方形範圍的圖片
                cropped_face = frame[y1:y2, x1:x2]

                # 確保裁剪出來的圖片大小不會超過要求的尺寸
                cropped_face_resized = cv2.resize(cropped_face, (image_size, image_size))

                # 保存裁剪後的圖片
                frame_filename = os.path.join(output_folder, f"face_{saved_count:04d}.jpg")
                cv2.imwrite(frame_filename, cropped_face_resized)

                saved_count += 1

    cap.release()
    print(f"Extracted {saved_count} face images to {output_folder}")

if __name__ == "__main__":
    # 設定命令行參數
    parser = argparse.ArgumentParser(description='Extract faces from a video.')
    parser.add_argument('video_path', type=str, nargs='?', default='target.mp4', help='Path to the video file')
    parser.add_argument('--output_folder', type=str, default='output/faces', help='Folder to save extracted faces')
    parser.add_argument('--image_size', type=int, default=256, help='Size of the square cropped face images')
    parser.add_argument('--fps', type=int, default=1, help='Frames per second to process')
    
    # 解析命令行參數
    args = parser.parse_args()

    # 執行提取人臉的函數
    extract_faces(args.video_path, args.image_size, args.output_folder, args.fps)