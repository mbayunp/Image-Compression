import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import os

data = pd.read_csv('Book1.csv')

# Menampilkan contoh dari font yang tersedia dengan pengambilan nama di kolom pertama Book1.csv
font_names = ['arial.ttf', 'calibri.ttf', 'times.ttf']

print("Pilihan Font yang Tersedia:")
for i, font_name in enumerate(font_names):
    print(f"{i+1}. {font_name}")

user_choice = int(input("Masukkan nomor font pilihan Anda (1-3): "))
selected_font = font_names[user_choice - 1]

# Memilih template sertifikat
template_choice = int(input("Pilih template sertifikat (1/2): "))
template_filename = f"sertifikat{template_choice}.png"

# Fungsi untuk membuat sertifikat
def create_certificate(name, cert_number, font, template):
    # Buka template sertifikat
    template_image = Image.open(template)
    draw = ImageDraw.Draw(template_image)
    
    # Tentukan ukuran teks
    font_size = 120
    
    # Tentukan posisi teks nama sertifikat
    font = ImageFont.truetype(font, size=font_size)
    text_width, text_height = draw.textsize(name, font)
    x = (template_image.width - text_width) / 2
    y = (template_image.height / 2.2) - text_height
    
    # Tambahkan nama peserta ke template
    draw.text((x, y), name, font=font, fill='black')
    
    # Simpan sertifikat dengan penamaan berurutan
    output_filename = f'sertifikat_{cert_number:03d}_{name}.png'
    template_image.save(output_filename)
    print(f'Sertifikat untuk {name} berhasil dibuat.')
    
    return output_filename

# Function to compress image
def compress_image(input_image_path, output_image_path, max_size):
    image = Image.open(input_image_path)
    image.thumbnail((max_size, max_size))
    image.save(output_image_path)

while True:
    # Pilih contoh data dari baris pertama
    first_row = data.iloc[0]
    example_name = first_row['name']

    # Membuat contoh sertifikat dengan font yang dipilih
    example_certificate = create_certificate(example_name, 0, selected_font, template_filename)

    # Menampilkan contoh sertifikat
    example_image = Image.open(example_certificate)
    plt.imshow(example_image)
    plt.axis("off")
    plt.show()

    # User prompt untuk melanjutkan atau memilih font lain
    continue_program = input("Apakah Anda ingin melanjutkan penamaan sertifikat dengan font ini? (ya/tidak): ")

    if continue_program.lower() == "tidak":
        break

    # List to store the generated image filenames
    image_files = []

    # Loop through the data to create certificates and store the filenames
    for index, row in data.iterrows():
        filename = create_certificate(row['name'], index + 1, selected_font, template_filename)
        image_files.append(filename)

    # Compress the generated images and display them
    for filename in image_files:
        compressed_filename = f"compressed_{filename}"
        compress_image(filename, compressed_filename, 500)  # Specify the maximum size (in pixels) you want for the compressed images

        # Get file size before compression
        before_size = os.path.getsize(filename)

        # Get file size after compression
        after_size = os.path.getsize(compressed_filename)

        # Display file sizes
        print(f"Ukuran file sebelum kompresi: {before_size} bytes")
        print(f"Ukuran file setelah kompresi: {after_size} bytes")

        # Display the compressed image
        image = Image.open(compressed_filename)
        plt.imshow(image)
        plt.axis("off")  # Hide the axes
        plt.show()
        