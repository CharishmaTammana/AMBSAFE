from pydub import AudioSegment

class AmbulanceSirenDetector:
    def __init__(self, threshold=0.1):
        self.threshold = threshold

    def detect_siren(self, audio_file_path):
        try:
            audio = AudioSegment.from_mp3(audio_file_path)
            data = audio.get_array_of_samples()

            magnitude = max(abs(min(data)), abs(max(data)))

            if magnitude > self.threshold:
                print("Ambulance siren detected!")
            else:
                print("No ambulance siren detected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    detector = AmbulanceSirenDetector(threshold=1000)  # Adjust threshold as needed
    audio_file_path = "D:\exeed new\sound.mp3"  # Replace with the actual file path
    detector.detect_siren(audio_file_path)
