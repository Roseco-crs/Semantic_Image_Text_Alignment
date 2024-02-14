from PIL import Image, ImageDraw

# Create a new image with white background
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")

# Create a draw object
draw = ImageDraw.Draw(image)

# Draw a red rectangle on the image
rectangle_coordinates = [(50, 50), (450, 450)]
draw.rectangle(rectangle_coordinates, outline="red", width=2)

# Save the image
image.save("generated_image.png")

# Display the image (optional)
image.show()
