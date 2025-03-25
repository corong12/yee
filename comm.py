import serial
import time

# 시리얼 포트 설정
PORT = "COM3"  # Windows의 경우 "COM3", 리눅스/Mac은 "/dev/ttyUSB0"
BAUDRATE = 9600  # 전송 속도

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"✅ {PORT}에 연결됨")

    while True:
        # "ping" 메시지 전송
        ser.write(b'ping\n')
        print("📤 Sent: ping")
        
        # 응답 수신
        response = ser.readline().decode().strip()
        if response:
            print(f"📥 Received: {response}")

        time.sleep(1)  # 1초 대기

except serial.SerialException as e:
    print(f"❌ 시리얼 포트 오류: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("🔌 연결 종료")
