

#Fungerar, men extremt långsam! Tar säkert fem minuter för en bild.
#Denna går mycket snabbare https://huggingface.co/spaces/mrfakename/OpenDalleV1.1-GPU-Demo




from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalleV1.1', torch_dtype=torch.float16).to('cuda')
image = pipeline('Donald trump riding on a missile with Kim Jon-Un applauding').images[0]
filename = "20250123_TrumpUn.jpg"

# Save the image
image.save(filename)
print("Image saved as generated_image.jpg")





