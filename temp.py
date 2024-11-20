from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 显示当前的日期和时间
print("当前日期和时间：", current_time)

# 格式化输出日期
print("当前日期：", current_time.strftime("%Y-%m-%d"))

# 格式化输出时间
print("当前时间：", current_time.strftime("%H:%M:%S"))

# 显示当前年份、月份和日期
print("当前年份：", current_time.year)
print("当前月份：", current_time.month)
print("当前日期：", current_time.day)

# 显示当前是星期几
print("今天是星期：", current_time.strftime("%A"))
