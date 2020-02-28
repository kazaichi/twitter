from tqdm import tqdm
import time
def counter(sec):
    print("429:Too Many Requests")
    print("速度制限にかかりました。")
    for i in tqdm(range(int(sec + 1))):
        time.sleep(1.0)