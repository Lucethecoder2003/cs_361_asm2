import time

while True:
    user_input = input("Enter 1 to generate a new image or 2 to exit: ")

    if user_input == '1':
        prng_file = open("Prng-Service.txt", "w")
        prng_file.write("run")
        prng_file.close()

        time.sleep(5)

        prng_file = open("Prng-Service.txt", "r")
        random_number = prng_file.read()
        prng_file.close()

        #print(f"Random number generated: {random_number}")

        img_file = open("Imgsrv.txt", "w")
        img_file.write(random_number)
        img_file.close()

        time.sleep(5)

        img_file = open('Imgsrv.txt', 'r')
        image_path = img_file.read().strip()
        print("Image path: " + image_path)
        img_file.close

    elif user_input == '2':
        break

    else:
        print("Unknown option")
