from PIL import Image, ImageDraw, ImageFont


W, H = 800, 1000
img = Image.new("RGB", (W, H), (240, 240, 240))  
draw = ImageDraw.Draw(img)
cx = W // 2  


logo = Image.open("86312.gif").convert("RGBA")  
logo = logo.resize((500, 300))  
lx, ly = logo.size
img.paste(logo, (cx - lx // 2, 20), logo)  


trophy_color = (0, 100, 120)   
accent_color = (230, 150, 50)  
black = (0, 0, 0)             


draw.polygon([(cx - 80, 300), (cx + 80, 300), (cx, 500)],
             outline=trophy_color, width=8)
draw.rectangle([cx - 20, 500, cx + 20, 540], outline=trophy_color, width=8)
draw.rectangle([cx - 40, 540, cx + 40, 580], outline=trophy_color, width=8)


draw.line([(cx - 160, 350), (cx - 100, 350)], fill=accent_color, width=6)
draw.line([(cx - 160, 380), (cx - 120, 380)], fill=accent_color, width=6)
draw.line([(cx + 100, 350), (cx + 160, 350)], fill=accent_color, width=6)
draw.line([(cx + 120, 380), (cx + 160, 380)], fill=accent_color, width=6)


try:
    font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 100)   
    font_small = ImageFont.truetype("DejaVuSans.ttf", 60)       
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()



bbox = draw.textbbox((0, 0), "INTRAMURALS", font=font_big)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text((cx - w // 2, 650), "INTRAMURALS", font=font_big, fill=black)


bbox = draw.textbbox((0, 0), "TOURNAMENT", font=font_small)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text((cx - w // 2, 770), "TOURNAMENT", font=font_small, fill=black)


output_path = "trophy_logo_with_himamat.png"
img.save(output_path)
img.show()
print(f"✅ Saved as {output_path}")

