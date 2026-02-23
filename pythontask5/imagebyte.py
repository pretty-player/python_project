import os

def process_image(source_path, destination_path):
    try:
        # 1. Open the source image in 'rb' (Read Binary) mode
        with open(source_path, 'rb') as source_file:
            image_data = source_file.read()
            
            # 2. Print the first 100 bytes
            print(f"--- First 100 Bytes of {source_path} ---")
            print(image_data[:100])
            print("\n" + "-"*40)
            
            # 3. Write the data to the destination in 'wb' (Write Binary) mode
            with open(destination_path, 'wb') as dest_file:
                dest_file.write(image_data)
                
        print(f"File successfully copied to: {destination_path}")
        print(f"Size: {len(image_data)} bytes")

    except FileNotFoundError:
        print("Error: Source image file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Execution ---
# Replace 'input.jpg' with your actual image filename
process_image('download.webp', 'copy_of_image.jpg')