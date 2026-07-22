import os
import google.generativeai as genai

# Gemini API Config
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY nahi mili!")
    exit(1)

genai.configure(api_key=GEMINI_API_KEY)

def generate_hisstron_post():
    prompt = """
    You are the lead content creator for 'Hisstron' - a brand dedicated to sharing authentic, inspirational stories of successful figures from around the world.
    
    Task:
    1. Select one highly influential or unique successful person from world history or modern era.
    2. Write a captivating, high-value social media post about their journey, major achievement, and 1 key lesson.
    3. Keep the tone inspiring, professional, and powerful.
    4. Include relevant hashtags at the end (#Hisstron #SuccessStories #Inspiration #Leadership).
    """
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    print("=== HISSTRON DAILY RESEARCH POST ===")
    print(response.text)
    print("====================================")

if __name__ == "__main__":
    generate_hisstron_post()
