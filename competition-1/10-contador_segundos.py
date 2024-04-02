seconds = int(input())
hours = (seconds // 3600)
minutes = (seconds % 3600) // 60
print(f'{hours}h {minutes}m {(seconds % 3600) % 60}s')