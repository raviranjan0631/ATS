FROM python:3.7

WORKDIR /app


# COPY model/ model/
COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt
RUN python3 -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); model.save('models')"

COPY src/ src/
COPY main.py main.py
ENV OPENAI_API_KEY=your_openai_key
CMD streamlit run main.py --server.port=80






