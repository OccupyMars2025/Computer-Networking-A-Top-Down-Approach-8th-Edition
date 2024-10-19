import base64

# Base64 string
base64_str = "d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms="

ascii_str = base64.b64decode(base64_str.encode('ascii')).decode('ascii')


print(f"2024 ASCII string: {ascii_str}")


base64_str_v2 = base64.b64encode(ascii_str.encode('ascii')).decode('ascii')

assert base64_str == base64_str_v2
