hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

end_hours = (hour + (mins + dura) // 60) % 24
end_minutes = (mins + dura) % 60

print(end_hours, ":", end_minutes)