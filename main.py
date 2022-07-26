import os

def main():
	print("Hello")
	token = os.environ.get("API_KEY")
	if not token:
		raise RunTimeError("Token not found")
	print("All good")

if __name__ == '__main__':
	main()
