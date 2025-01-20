
#Följde denna video. Häftigt!
#https://www.youtube.com/watch?v=_5F-toek0G8
#Fick den att funka i google colab



from diffusers import AudioLDM2Pipeline
import gradio as gr
import torch

model_id = "cvssp/audioldm2"
pipe = AudioLDM2Pipeline.from_pretrained(model_id,
                                         torch_dtype = torch.float16,
                                         ).to("cuda")


generator = torch.Generator("cuda").manual_seed(0)


def create_music(prompt):
  negative_prompt = "Low quality"

  audio = pipe(
      prompt,
      negative_prompt = negative_prompt,
      audio_length_in_s = 10,
      generator = generator,
  ).audios[0]

  return 16000, audio

interface = gr.Interface(
    title = "Music Generation App",
    examples = ["Tin whistle jig"],
    fn = create_music,
    inputs = gr.Textbox(),
    outputs = "audio",
).launch(debug=True, share=True)