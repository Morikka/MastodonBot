import retirenow
import data

if __name__ == "__main__":
    message = data.GenerateMessage()
    print(message)
    retirenow.posting(message)