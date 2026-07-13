"""Render 무료 플랜 spin-down 방지용 keep-alive 스크립트.

노트북에서 상시 실행:
    python keepalive.py https://<your-app>.onrender.com

10분마다 /health 를 호출해 서버가 잠들지 않게 유지한다.
(Render 무료 서비스는 15분 동안 요청이 없으면 잠들고, 깨는 데 30~60초 걸림)

노트북이 잠자기 상태가 되면 ping도 멈추므로, PlayMCP 심사 기간에는
cron-job.org (무료) 에 같은 URL을 10분 간격으로 등록해 두는 것을 권장.
"""

import sys
import time
from datetime import datetime

import requests

INTERVAL_SECONDS = 600  # 10분


def main() -> None:
    if len(sys.argv) < 2:
        print("사용법: python keepalive.py https://<your-app>.onrender.com")
        sys.exit(1)

    url = sys.argv[1].rstrip("/") + "/health"
    print(f"keep-alive 시작: {url} ({INTERVAL_SECONDS}초 간격)")

    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            r = requests.get(url, timeout=70)  # 콜드스타트(최대 60초) 대기 여유
            print(f"[{now}] {r.status_code} {r.text.strip()[:80]}")
        except requests.exceptions.RequestException as e:
            print(f"[{now}] ping 실패: {e}")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
