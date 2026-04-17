from PIL import Image
import requests
from io import BytesIO


def encode_text(text, use_random_img, img_url = None, key= 20,
                default_img_path = None , output_path="encoded_img.png"): 
    """
    Encodes text into selected image pixels and saves the result as a PNG image.

    Args:
        text: The input text to encode.
        use_random_img: Whether to fetch a random image.
        img_url: URL of a user-provided image.
        key: Pixel step size used for encoding.
        default_img_path: Optional fallback image path.

    Returns:
        PIL.Image.Image or None: The encoded image if successful, otherwise None.
    """
    
    if not use_random_img: 
        try: 
            response = requests.get(img_url , timeout=10)
            response.raise_for_status() # catches for HTTP errors 
            
            img = Image.open(BytesIO(response.content)).convert("RGB")
            print("GOT THE IMAGE YOU CHOSE SUCCESSFULLY")

        except requests.exceptions.RequestException as e:
            print("Failed to download the image:", e)
            return None
        except (Image.UnidentifiedImageError, OSError) as e:
            print("Downloaded data is not a valid image:", e)
            return None
    else: # we should pick a random image from web here
        try: 
            random_pic_url = "https://picsum.photos/400/300"
            response = requests.get(random_pic_url, timeout=3)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGB")

        except requests.exceptions.RequestException:
            if default_img_path is None:
                print("Could not fetch a random image, and no default image was provided.")
                return None
            img = Image.open(default_img_path).convert("RGB")
    
    # now we have the image and the code_text
    
    
    pixels = img.load()
    positions = []
    for i in range(0, img.size[0] , key):
        for j in range(0, img.size[1] , key):
            #pixels[i, j] = (ord(char), 0, 0) #changes will applied on the RED part of the image
            positions.append((i,j))
            
            
            
    text_to_store = text + "\0"
    
    if len(text_to_store) > len(positions):
        print("This text is too long for this picture!!!")
        return None
    
    for idx, char in enumerate(text_to_store):
        i, j = positions[idx]
        r, g, b = pixels[i, j]
        pixels[i, j] = (ord(char), g, b)
        
    img.save(output_path)
    return img

        
        
def decode_text(img_path,  key=20):
    """
    we get the image in the input and decode it in the string
    """
    try: 
        img = Image.open(img_path).convert("RGB")
    except FileNotFoundError as e:
        print(f"Image path is not correct.\n{e}")
        return None
    except OSError as e:
        print(f"Could not open the image.\n{e}")
        return None

    
    string_code = []
    pixels = img.load()
    
    for i in range(0, img.size[0], key) :
        for j in range(0, img.size[1], key):
            (tmp, _, _) = pixels[i, j]
            ch = chr(tmp)
            if ch == "\0":
                return "".join(string_code)
            string_code.append(ch)
            
    
    return "".join(string_code)
    
            
        
     

