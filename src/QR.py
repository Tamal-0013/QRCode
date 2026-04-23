import qrcode
import os

def generate_qr(data, filename="my_qr_image.png", output_folder="output"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    #add data
    qr.add_data(data)

    #gen QR
    qr.make(fit=True)

    #create image 
    img = qr.make_image(fill_color="black", back_color="white")

    #save image
    full_path = os.path.join(output_folder, filename)
    img.save(full_path)

    # Tell the user it worked
    print(f"✅ QR code saved as: {filename}")
    print(f"📱 It contains: {data}")


if __name__ == "__main__":
    # This is my first test
    test_message = "i know how to make qr code"
    generate_qr(test_message, "my_first_qr.png")