from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load pre-trained T5 model and tokenizer
model_name = "t5-small"  # You can also try 't5-base', 't5-large', etc.
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to generate a summary
def generate_summary(text):
    # Preprocess the text by encoding it
    input_ids = tokenizer.encode(f"summarize: {text}", return_tensors="pt", max_length=512, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    # Decode the output to text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example CV data to summarize
cv_text = """
John Doe is a senior software engineer with over 8 years of experience. He has worked at multiple organizations including TechCorp and SoftWorks, specializing in backend development, cloud services, and team management. He is proficient in Python, Java, and cloud platforms like AWS. He has led a team of 5 engineers and worked on various projects involving scalable microservices architecture. He is passionate about continuous learning and regularly contributes to open-source projects.
"""

# Generate summary
summary = generate_summary(cv_text)
print("Generated CV Summary:", summary)
