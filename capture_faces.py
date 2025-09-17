import cv2
import os 
import sqlite3
from datetime import datetime

##----##
def init_database():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
              (student_id TEXT PRIMARY KEY, name TEXT, register_date DATE)''')
    conn.commit()
    return conn

##----##
def create_dataset_folder(student_id):
    """ถ้าไม่มีข้อมูลของที่กรอกมาให้สร้าง folder สำหรับ เก็บรูปของนักศึกษา"""
    path = f"dataset/{student_id}"
    if not os.path.exists(path):
        os.makedirs(path)
        return path

def capture_face():
    conn = init_database()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error : ไม่สามารถเปิดกล้องได้")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fromtalface_default.xml')

    # เก็บข้อมูลนักเรียน
    while True:
        student_id = input("Enter STUDENT ID : ").strip()
        if not student_id:
            print("Error: โปรดกรอกรหัสนักศึกษา")
            continue

    # ตรวจสอบว่ามีรหัสนักศึกษาแล้วรึยัง
        cursor = conn.cursor()
        cursor.excute("เลือกชื่อจากนักเรียน จาก student_id = ?" , (student_id,))
        existing_student = cursor.fetchone()

        if existing_student:
            print(f"รหัสนักศึกษา {student_id} มีอยู่แล้ว ชื่อ : {existing_student[0]}")
            choice = input("")