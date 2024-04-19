import subprocess
import time
if __name__ == '__main__':
    subprocess.run(["python", "./Crawler.py"])
    time.sleep(10)
    subprocess.run(["python", "./DataIngestion.py"])
