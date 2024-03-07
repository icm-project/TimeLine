import serial
import pygame
import threading
from pygame.locals import *

ser = serial.Serial('/dev/ttyACM0', 9600)

# Initialize pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((1920, 1024))
pygame.display.set_caption("Image Viewer")

# Define the values and corresponding image file names
image_mapping = {
    1: '/home/ICM/Desktop/TL/1904-1.jpg',        
    90: '/home/ICM/Desktop/TL/1904-2.jpg',
    135: '/home/ICM/Desktop/TL/1904-3.jpg',
    
    200: '/home/ICM/Desktop/TL/1943.jpg',
    
    270: '/home/ICM/Desktop/TL/1945-1.jpg',
    293: '/home/ICM/Desktop/TL/1945-2.jpg',
    316: '/home/ICM/Desktop/TL/1945-3.jpg',
    339: '/home/ICM/Desktop/TL/1945-4.jpg',
    362: '/home/ICM/Desktop/TL/1945-5.jpg',
    
    390: '/home/ICM/Desktop/TL/1947-1.jpg',
    400: '/home/ICM/Desktop/TL/1947-2.jpg',
    410: '/home/ICM/Desktop/TL/1947-3.jpg',
    420: '/home/ICM/Desktop/TL/1947-4.jpg',
    430: '/home/ICM/Desktop/TL/1947-5.jpg',
    
    443: '/home/ICM/Desktop/TL/1948-1.jpg',
    500: '/home/ICM/Desktop/TL/1948-2.jpg',
    
    550: '/home/ICM/Desktop/TL/1950.jpg',
    
    609: '/home/ICM/Desktop/TL/1951-1.jpg',
    687: '/home/ICM/Desktop/TL/1951-2.jpg',
    
    775: '/home/ICM/Desktop/TL/1954-1.jpg',
    800: '/home/ICM/Desktop/TL/1954-2.jpg',
    830: '/home/ICM/Desktop/TL/1954-3.jpg',
    
    860: '/home/ICM/Desktop/TL/1957-1.jpg',
    900: '/home/ICM/Desktop/TL/1957-2.jpg',
    
    940: '/home/ICM/Desktop/TL/1958-1.jpg',
    950: '/home/ICM/Desktop/TL/1958-2.jpg',
    960: '/home/ICM/Desktop/TL/1958-3.jpg',
    970: '/home/ICM/Desktop/TL/1958-4.jpg',
    980: '/home/ICM/Desktop/TL/1958-5.jpg',
    
    990: '/home/ICM/Desktop/TL/1959.jpg',
    
    1000: '/home/ICM/Desktop/TL/1962-1.jpg',
    1010: '/home/ICM/Desktop/TL/1962-2.jpg',
    1020: '/home/ICM/Desktop/TL/1962-3.jpg',
    1030: '/home/ICM/Desktop/TL/1962-4.jpg',
    1040: '/home/ICM/Desktop/TL/1962-5.jpg',
    
    1045: '/home/ICM/Desktop/TL/1963-1.jpg',
    1080: '/home/ICM/Desktop/TL/1963-2.jpg',
    1130: '/home/ICM/Desktop/TL/1963-3.jpg',
    1170: '/home/ICM/Desktop/TL/1963-4.jpg',
    
    
    1200: '/home/ICM/Desktop/TL/1965.jpg',
    1240: '/home/ICM/Desktop/TL/1965-2.jpg',
    
    1270: '/home/ICM/Desktop/TL/1968.jpg',
    
    1300: '/home/ICM/Desktop/TL/1969-1.jpg',
    1370: '/home/ICM/Desktop/TL/1969-2.jpg',
    
    1435: '/home/ICM/Desktop/TL/1970.jpg',
    
    1450: '/home/ICM/Desktop/TL/1971-1.jpg',
    1455: '/home/ICM/Desktop/TL/1971-2.jpg',
    1460: '/home/ICM/Desktop/TL/1971-3.jpg',
    1465: '/home/ICM/Desktop/TL/1971-4.jpg',
    1470: '/home/ICM/Desktop/TL/1971-5.jpg',
    1475: '/home/ICM/Desktop/TL/1971-6.jpg',
    1480: '/home/ICM/Desktop/TL/1971-7.jpg',
    
    1490: '/home/ICM/Desktop/TL/1972-1.jpg',
    1520: '/home/ICM/Desktop/TL/1972-2.jpg',
    1545: '/home/ICM/Desktop/TL/1972-3.jpg',
    1570: '/home/ICM/Desktop/TL/1972-4.jpg',
    1585: '/home/ICM/Desktop/TL/1972-5.jpg',
    
    1620: '/home/ICM/Desktop/TL/1974.jpg',
    
    1725: '/home/ICM/Desktop/TL/1976-1.jpg',
    1730: '/home/ICM/Desktop/TL/1976-2.jpg',
    1735: '/home/ICM/Desktop/TL/1976-3.jpg',
    1740: '/home/ICM/Desktop/TL/1976-4.jpg',
    
    1745: '/home/ICM/Desktop/TL/1978-1.jpg',
    1845: '/home/ICM/Desktop/TL/1978-2.jpg',
    
    1930: '/home/ICM/Desktop/TL/1980.jpg',
    
    1950: '/home/ICM/Desktop/TL/1981-1.jpg',
    1965: '/home/ICM/Desktop/TL/1981-2.jpg',
    1980: '/home/ICM/Desktop/TL/1981-3.jpg',
    1995: '/home/ICM/Desktop/TL/1981-4.jpg',
    
    2010: '/home/ICM/Desktop/TL/1982-1.jpg',
    2035: '/home/ICM/Desktop/TL/1982-2.jpg',
    2060: '/home/ICM/Desktop/TL/1982-3.jpg',
    
    2080: '/home/ICM/Desktop/TL/1983.jpg',
    2105: '/home/ICM/Desktop/TL/1983-2.jpg',
    
    2126: '/home/ICM/Desktop/TL/1984-1.jpg',
    2150: '/home/ICM/Desktop/TL/1984-2.jpg',
    2170: '/home/ICM/Desktop/TL/1984-3.jpg',
    
    2195: '/home/ICM/Desktop/TL/1985-1.jpg',
    2215: '/home/ICM/Desktop/TL/1985-2.jpg',
    2235: '/home/ICM/Desktop/TL/1985-3.jpg',
    
    2260: '/home/ICM/Desktop/TL/1987-1.jpg',
    2300: '/home/ICM/Desktop/TL/1987-2.jpg',
    
    2345: '/home/ICM/Desktop/TL/1988-1.jpg',
    2395: '/home/ICM/Desktop/TL/1988-2.jpg',
    
    2435: '/home/ICM/Desktop/TL/1989-1.jpg',
    2470: '/home/ICM/Desktop/TL/1989-2.jpg',
    2505: '/home/ICM/Desktop/TL/1989-3.jpg',
    
    2533: '/home/ICM/Desktop/TL/1991-1.jpg',
    2545: '/home/ICM/Desktop/TL/1991-2.jpg',
    2553: '/home/ICM/Desktop/TL/1991-3.jpg',
    
    2560: '/home/ICM/Desktop/TL/1992-1.jpg',
    2573: '/home/ICM/Desktop/TL/1992-2.jpg',
    
    2581: '/home/ICM/Desktop/TL/1993-1.jpg',
    2661: '/home/ICM/Desktop/TL/1993-2.jpg',
    
    2736: '/home/ICM/Desktop/TL/1994-1.jpg',
    2742: '/home/ICM/Desktop/TL/1994-2.jpg',
    2748: '/home/ICM/Desktop/TL/1994-3.jpg',
    2754: '/home/ICM/Desktop/TL/1994-4.jpg',
    
    2758: '/home/ICM/Desktop/TL/1995-1.jpg',
    2767: '/home/ICM/Desktop/TL/1995-2.jpg',
    2775: '/home/ICM/Desktop/TL/1995-3.jpg',
    2783: '/home/ICM/Desktop/TL/1995-4.jpg',
    
    2792: '/home/ICM/Desktop/TL/1997-1.jpg',
    2862: '/home/ICM/Desktop/TL/1997-2.jpg',
    
    2926: '/home/ICM/Desktop/TL/1998.jpg',
    
    2961: '/home/ICM/Desktop/TL/1999.jpg',
    
    3004: '/home/ICM/Desktop/TL/2000.jpg',
    
    3054: '/home/ICM/Desktop/TL/2001-1.jpg',
    3147: '/home/ICM/Desktop/TL/2001-2.jpg',
    
    3229: '/home/ICM/Desktop/TL/2006-1.jpg',
    
    3264: '/home/ICM/Desktop/TL/2007-1.jpg',
    3283: '/home/ICM/Desktop/TL/2007-2.jpg',
    
    3295: '/home/ICM/Desktop/TL/2008-1.jpg',
    3315: '/home/ICM/Desktop/TL/2008-2.jpg',
    
    3336: '/home/ICM/Desktop/TL/2009.jpg',
    
    3541: '/home/ICM/Desktop/TL/2011-1.jpg',
    3557: '/home/ICM/Desktop/TL/2011-2.jpg',
    
    3569: '/home/ICM/Desktop/TL/2012.jpg',
    
    3615: '/home/ICM/Desktop/TL/2021.jpg',
    
    3666: '/home/ICM/Desktop/TL/2022.jpg',
    

}
        

# Create a Pygame surface for image display
image_surface = pygame.Surface((1920, 1024))

def display_image(image_filename):
    img = pygame.image.load(image_filename)
    #img = pygame.transform.scale(img, (800, 600))  # Resize the image to fit the window (adjust as needed)
    image_surface.blit(img, (0, 0))

def read_encoder_values():
    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                encoder_value = int(data)
                print(encoder_value)
          
                if encoder_value in image_mapping:
                    # Clear the image_surface
                    image_surface.fill((0, 0, 0))  # Fill with a black color
                    image_filename = image_mapping[encoder_value]
                    display_image(image_filename)
        except KeyboardInterrupt:
            break
    
def main():
    # Create a thread for reading encoder values
    encoder_thread = threading.Thread(target=read_encoder_values)
    encoder_thread.start()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update the Pygame window with the current image
        screen.blit(image_surface, (0, 0))
        pygame.display.flip()

    # Wait for the encoder thread to finish
    encoder_thread.join()

    ser.close()
    pygame.quit()

if __name__ == "__main__":
    main()

