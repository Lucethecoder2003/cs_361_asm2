import time

# There are 10 images
number_of_images = 10

while True:
    time.sleep(1)

    with open('Imgsrv.txt', 'r+') as file:
        content = file.read().strip()

        if content.isdigit():
            number = int(content)

            modded_number = number % number_of_images
            file.seek(0)
            file.truncate()

            # Write the path to the corresponding image file
            file.write(rf'C:\Users\tudlu\Desktop\cs_361\assignment_1\images_folder\image_{modded_number}.png')

