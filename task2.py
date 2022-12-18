import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        file_opened = open(f'{file}', mode='rb')
        f = file_opened.read()
    except FileNotFoundError as e:
        print(e)
        print(f'Time required for {file} = 0.0')

    else:
        print(f'Time required for {file} = {time.time() - start_time}')
    finally:
        file_opened.close()


video_data = read_file_timed('my_file.txt')  # 155 MB
# Time required for video.mp4 = 0.06553506851196289
video_data = read_file_timed('file_not_exist.mp4')  # 155 MB
# FileNotFoundError: [Errno 2] No such file or directory: 'video2.mp4'
# Time required for video2.mp4 = 0.0
