import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk, messagebox

ser = None  # 시리얼 객체

def connect_serial():
    global ser
    port = port_combobox.get()
    baudrate = baudrate_combobox.get()
    
    if not port or not baudrate:
        messagebox.showerror("오류", "포트와 Baudrate를 선택하세요!")
        return
    
    try:
        ser = serial.Serial(port, int(baudrate), timeout=1)
        status_label.config(text="연결 상태: 연결됨", fg="green")
        messagebox.showinfo("연결 성공", f"{port}에 연결되었습니다!")
    except serial.SerialException as e:
        messagebox.showerror("연결 실패", str(e))

def send_ping():
    global ser
    if ser and ser.is_open:
        ser.write(b'ping\n')
        response = ser.readline().decode().strip()
        output_text.insert(tk.END, f"📤 Sent: ping\n")
        if response:
            output_text.insert(tk.END, f"📥 Received: {response}\n")
    else:
        messagebox.showerror("오류", "먼저 시리얼 연결을 해주세요!")

# GUI 생성
root = tk.Tk()
root.title("시리얼 통신 테스트")
root.geometry("400x300")

# 포트 선택 드롭다운
ttk.Label(root, text="포트 선택:").pack(pady=5)
ports = [port.device for port in serial.tools.list_ports.comports()]
port_combobox = ttk.Combobox(root, values=ports)
port_combobox.pack()

# 전송 속도 선택
ttk.Label(root, text="Baudrate:").pack(pady=5)
baudrate_combobox = ttk.Combobox(root, values=[9600, 115200])
baudrate_combobox.pack()

# 연결 상태 표시
status_label = tk.Label(root, text="연결 상태: 해제됨", fg="red")
status_label.pack(pady=5)

# 버튼 추가
connect_button = tk.Button(root, text="연결하기", command=connect_serial)
connect_button.pack(pady=5)

ping_button = tk.Button(root, text="Ping 보내기", command=send_ping)
ping_button.pack(pady=5)

# 응답 표시창
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# GUI 실행
root.mainloop()
