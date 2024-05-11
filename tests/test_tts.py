from tts import ParlerTTS
import soundfile as sf


def test_tts():
    tts = ParlerTTS('parler-tts/parler_tts_mini_v0.1', 'cuda:0', '../checkpoints')

    prompt = "Hey, how are you doing today?"
    description = "A female speaker with a slightly low-pitched voice delivers her words quite expressively, in a very confined sounding environment with clear audio quality. She speaks very fast."

    audio_arr = tts.generate(description, prompt)
    sf.write("parler_tts_out.wav", audio_arr, tts.sampling_rate)
