def format_strings(*args):      # ตั้งชื่อฟังก์ชันว่า format_strings และสามารถรับตัวอักษรได้หลายตัว
    combined_string = "".join(args)     # จะรวมอักษรทั้งหมดโดยไม่มีตัวคั่น
    formatted_string = combined_string.upper()      # ให้เปลี่ยนอักษรพิมพ์เล็กเป็นพิมพ์ใหญ่
    if''in combined_string:     # ตรวจสอบว่าในข้อความมีช่องว่างอยู่หรือไม่
        formatted_string = formatted_string.replace(" ", "-")       # ให้แทนที่ ที่มีช่องว่างด้วย -
    return formatted_string     # ตรวจสอบว่าในที่ว่างถูกแทนที่ด้วย - หรือยังถ้ายังให้กับไปทำใหม่

if __name__ == "__main__":
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result) # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result) # Output: "PYTHOISFUN"

    result = format_strings("Concatenate", "these", "strings", "please")
    print(result) # Output: "CONCATENATETHESESTRINGSPLEASE"
    
    result = format_strings("Hello world")
    print(result) # Output: "HELLO-WORLD"