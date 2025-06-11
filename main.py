from dotenv import load_dotenv
import os

load_dotenv()

def main():
    key = os.getenv("api_key")
    print("Hello from zoomcamp!")
    print(key)


if __name__ == "__main__":
    main()
