import asyncio
import edge_tts

VOICE = "en-US-AndrewNeural"  # Choose a voice
RATE = "+0%"                  # Speaking speed adjustment
OUTPUT_FILE = "output.mp3"    # File to save audio

async def main():
    text = "Hello to smooth Code youtube Channel."
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
