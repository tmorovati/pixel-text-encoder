# This project is about
# 1. read the IMAGE + get the text from input
# 2. turn the text into ascii code - put it in the RGB of the image
# 3. from the other side get the image and find the text 

# Ask GPT if we write a class for this projecT? 

     
from steganography import encode_text, decode_text


if __name__ == "__main__":
    key = 20
    while True: 
        print("\n--- Image Text Encoder ---")
        print("Hide text inside an image and decode it later.")
        print("1. Turn TEXT into IMAGE")
        print("2. Turn IMAGE into TEXT")
        print("Type 'exit' to quit.")
        
        choice_input = input("PRESS 1 OR 2 : ").strip().lower()

        if choice_input in ["exit" , "0" , "EXIT"]:
            print("Goodbye!")
            break
        
        try: 
            user_choice = int(choice_input)
            if user_choice not in [1, 2]:
                print("Please enter 1 or 2.")
                continue 
                
        except ValueError: 
            print("!!! INVALID INPUT. Please enter a number (1 or 2) !!!")
            continue
        
        
        
        

                
        if user_choice == 1: # Handle Option 1: Text to image
            print("WHAT IS THE TEXT YOU WANT TO ENCODE?")
            input_text = input(" >> ")
            if not input_text:
                print(f"Input text cannot be empty.")
                continue
            
            while True:
                try:
                    print("Choose image source:")
                    print("1. Use my image URL")
                    print("2. Use a random image")
                    print("3. Go back")

                    image_choice = int(input("Enter your choice: ").strip())
                except ValueError:
                    print("Please enter 1, 2, or 3.")
                    continue

                if image_choice == 1:
                    img_url = input("Enter the image URL: ").strip()
                    img = encode_text(input_text, use_random_img=False, img_url=img_url, key=key)
                    if img is not None:
                        img.show()
                    break

                elif image_choice == 2:
                    img = encode_text(input_text, use_random_img=True, key=key)
                    if img is not None:
                        img.show()
                    break

                elif image_choice == 3:
                    break

                else:
                    print("Please enter 1, 2, or 3.")
                

        elif user_choice == 2 : # Hanlde Option 2
            decoded_text = None
            while decoded_text is None: 
            
                print("GIVE ME THE ADDRESS OF YOUR IMAGE!!! \n")
                img_path = input(" >>").strip()
                decoded_text = decode_text(img_path=img_path)
                print(f"THIS IS YOUR CODE  >>>>>> {decoded_text} \n")

        else: 
            print("Invalid option.")


