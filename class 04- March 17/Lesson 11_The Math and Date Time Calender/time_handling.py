import time
# get current ticks since epoch
ticks = time.time()
print("⏱️ Ticks since epoch: ",ticks)

#2. convert to local time tuple
local_time = time.localtime(ticks)
print("\n📅 Local time tuple: ")
print(local_time)

#3. Convert to UTC time tuple
utc_time = time.gmtime(ticks)
print("\n🌐 UTC time tuple: ")
print(local_time)

#4.Get readable formatted time
formatted = time.asctime(local_time)
print("\n🕒 Formatted local time: ", formatted)

#5.format time using strftime()
formatted_custom = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print("🧾 Custom formatted time: ",formatted_custom)


#6. Pause for 2 seconds
print("\n⏳ Pausing for 2 seconds.... ")
time.sleep(2)
print("✅ Done!")




















