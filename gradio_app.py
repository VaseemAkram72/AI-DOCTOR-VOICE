# # # if you dont use pipenv uncomment the following:
# # # from dotenv import load_dotenv
# # # load_dotenv()

# # #VoiceBot UI with Gradio
# # import os
# # import gradio as gr

# # from brain_of_the_doctor import encode_image, analyze_image_with_query
# # from voice_of_the_patient import record_audio, transcribe_with_groq
# # from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

# # #load_dotenv()

# # system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
# #             What's in this image?. Do you find anything wrong with it medically? 
# #             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
# #             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
# #             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
# #             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
# #             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# # def process_inputs(audio_filepath, image_filepath):
# #     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
# #                                                  audio_filepath=audio_filepath,
# #                                                  stt_model="whisper-large-v3")

# #     # Handle the image input
# #     if image_filepath:
# #         doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
# #     else:
# #         doctor_response = "No image provided for me to analyze"

# #     voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 

# #     return speech_to_text_output, doctor_response, voice_of_doctor


# # # Create the interface
# # iface = gr.Interface(
# #     fn=process_inputs,
# #     inputs=[
# #        gr.Audio(type="filepath", label="Doctor Voice"), 
# #         gr.Image(type="filepath")
# #     ],
# #     outputs=[
# #         gr.Textbox(label="Speech to Text"),
# #         gr.Textbox(label="Doctor's Response"),
# #         gr.Audio(type="filepath", label="Doctor's Voice")
# #     ],
# #     title="AI Doctor with Vision and Voice"
# # )

# # iface.launch(debug=True)

# # #http://127.0.0.1:7860


# # if you dont use pipenv uncomment the following:


# from dotenv import load_dotenv
# load_dotenv()

# # VoiceBot UI with Gradio
# import os
# import gradio as gr

# from brain_of_the_doctor import (
#     encode_image,
#     analyze_image_with_query
# )

# from voice_of_the_patient import (
#     transcribe_with_groq
# )

# from voice_of_the_doctor import (
#     text_to_speech_with_elevenlabs
# )


# # System Prompt
# system_prompt = """
# You have to act as a professional doctor.

# Analyze the image carefully and respond naturally like a real doctor.

# Keep your response concise and human-like.
# Do not use markdown.
# Maximum 2 sentences only.
# """


# # Main Function
# def process_inputs(audio_filepath, image_filepath):

#     try:

#         # Check API Keys
#         groq_api = os.environ.get("GROQ_API_KEY")
#         elevenlabs_api = os.environ.get("ELEVENLABS_API_KEY")

#         if not groq_api:
#             return (
#                 "GROQ API KEY Missing",
#                 "Please check your .env file",
#                 None
#             )

#         if not elevenlabs_api:
#             return (
#                 "ELEVENLABS API KEY Missing",
#                 "Please check your .env file",
#                 None
#             )

#         # Speech To Text
#         speech_to_text_output = transcribe_with_groq(
#             GROQ_API_KEY=groq_api,
#             audio_filepath=audio_filepath,
#             stt_model="whisper-large-v3"
#         )

#         # Image Analysis
#         if image_filepath:

#             encoded_image = encode_image(image_filepath)

#             doctor_response = analyze_image_with_query(
#                 query=system_prompt + speech_to_text_output,
#                 encoded_image=encoded_image,
#                 model="meta-llama/llama-4-scout-17b-16e-instruct"
#             )

#         else:

#             doctor_response = "No image provided."

#         # Text To Speech
#         text_to_speech_with_elevenlabs(
#             input_text=doctor_response,
#             output_filepath="final.mp3"
#         )

#         # Return Outputs
#         return (
#             speech_to_text_output,
#             doctor_response,
#             "final.mp3"
#         )

#     except Exception as e:

#         return (
#             f"Error: {str(e)}",
#             f"Error: {str(e)}",
#             None
#         )


# # Gradio Interface
# iface = gr.Interface(

#     fn=process_inputs,

#     inputs=[

#         gr.Audio(
#             sources=["microphone"],
#             type="filepath",
#             label="Patient Voice"
#         ),

#         gr.Image(
#             type="filepath",
#             label="Medical Image"
#         )

#     ],

#     outputs=[

#         gr.Textbox(
#             label="Speech to Text"
#         ),

#         gr.Textbox(
#             label="Doctor's Response"
#         ),

#         gr.Audio(
#             type="filepath",
#             label="Doctor Voice"
#         )

#     ],

#     title="AI Doctor with Vision and Voice",

#     description="Upload a medical image and speak your symptoms.",

#     theme="soft"
# )


# # Launch App
# iface.launch(debug=True)

from dotenv import load_dotenv
load_dotenv()

# VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_the_doctor import (
    encode_image,
    analyze_image_with_query
)

from voice_of_the_patient import (
    transcribe_with_groq
)

from voice_of_the_doctor import (
    text_to_speech_with_elevenlabs
)


# System Prompt
system_prompt = """
You have to act as a professional doctor.

Analyze the image carefully and respond naturally like a real doctor.

Keep your response concise and human-like.
Do not use markdown.
Maximum 2 sentences only.
"""


# Main Function
def process_inputs(audio_filepath, image_filepath):

    try:

        # Load API Keys
        groq_api = os.getenv("GROQ_API_KEY")
        elevenlabs_api = os.getenv("ELEVENLABS_API_KEY")

        # Check API Keys
        if not groq_api:
            return (
                "GROQ API KEY Missing",
                "Please check your .env file",
                None
            )

        if not elevenlabs_api:
            return (
                "ELEVENLABS API KEY Missing",
                "Please check your .env file",
                None
            )

        # Check Audio Input
        if audio_filepath is None:
            return (
                "No audio detected",
                "Please record your voice",
                None
            )
        print("Audio Path:", audio_filepath)
        print("Image Path:", image_filepath)

        # Speech To Text
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=groq_api,
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )

        # Image Analysis
        if image_filepath is not None:

            encoded_image = encode_image(image_filepath)

            doctor_response = analyze_image_with_query(
                query=system_prompt + " " + speech_to_text_output,
                encoded_image=encoded_image,
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )

        else:

            doctor_response = (
                "No medical image was uploaded."
            )

        # Voice Output File
        output_voice_path = "final.mp3"

        # Text To Speech
        text_to_speech_with_elevenlabs(
            input_text=doctor_response,
            output_filepath=output_voice_path
        )

        # Return Final Outputs
        return (
            speech_to_text_output,
            doctor_response,
            output_voice_path
        )

    except Exception as e:

        return (
            f"Error: {str(e)}",
            f"Error: {str(e)}",
            None
        )


# Gradio Interface
iface = gr.Interface(

    fn=process_inputs,

    inputs=[

        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Patient Voice"
        ),

        gr.Image(
            type="filepath",
            label="Medical Image"
        )

    ],

    outputs=[

        gr.Textbox(
            label="Speech to Text"
        ),

        gr.Textbox(
            label="Doctor's Response"
        ),

        gr.Audio(
            type="filepath",
            label="Doctor Voice"
        )

    ],

    title="AI Doctor with Vision and Voice",

    description="Upload a medical image and speak your symptoms.",

    theme="soft"
)


# Launch App
iface.launch(debug=True)