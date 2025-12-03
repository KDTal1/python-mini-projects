import os, random, pygame, time

def dir_files(dir_path): # returns list of files in scream_library
    if not os.path.isdir(dir_path):
        print(f"{dir_path} is not a directory.")
        return
    
    files = os.listdir(dir_path)
    return random.choice(files)

def play_sound(sound_file_path):
    if not os.path.exists(sound_file_path):
        print(f"Error: Sound file not found at '{sound_file_path}'")
        print("Please make sure the SOUND_FILE variable is set correctly.")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file_path)
        print(f"Playing {sound_file_path}...")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error as e:
        print(f"Couldn't play sound: {e}")


if __name__ == "__main__":
    print(f"Current list of audio: {dir_files("scream_library")}") 
    play_sound(f"scream_library/{dir_files('scream_library')}")