import sqlite3

# اتصال به دیتابیس (اگر وجود نداشته باشه ساخته میشه)
conn = sqlite3.connect('my_database.db')

# ساخت cursor برای اجرای دستورات SQL
cursor = conn.cursor()

# ساخت یک جدول نمونه
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    scores INTEGER 
)
''')

# ذخیره تغییرات
conn.commit()

# بستن اتصال
conn.close()