import pygame

# Initialize pygame mixer for playing sound
pygame.mixer.init()

def play_fall_song(song_path="fall_alert.mp3"):
    """
    Plays the fall alert song when a fall is detected.
    """
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Optional: Wait until the song is done before continuing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check every 10ms if the music has finished
