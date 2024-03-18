# Use a pipeline as a high-level helper
from transformers import pipeline

#convercational pipeline
pipe = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")
