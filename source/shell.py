import traceback
import pip

print("python portable shell by alexdieu")
print("v1.0")
while True:
    user = input('''>>>''')
    try:
        exec(user)
    except Exception:
        traceback.print_exc()