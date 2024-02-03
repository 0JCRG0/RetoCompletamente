import os
from psycopg2.extensions import cursor
import numpy as np
import pandas as pd
import pretty_errors
import io
import logging
import requests
from tenacity import retry, wait_exponential, retry_if_exception_type, before_sleep_log, stop_after_attempt
import json
from dotenv import load_dotenv
import logging
import pandas as pd
from pdfminer.converter import TextConverter
from openai import OpenAI
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import magic
import pyclamd
import re
import ast


from .prompts import *
#from .main_utils import ConvertingToJsonObject, whether_json_object
import os
import together

load_dotenv('.env')
TOGETHER_API_KEY = os.environ.get("TOGETHER_AI_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
together.api_key = os.environ.get("TOGETHER_AI_API_KEY")
SAVE_PATH = os.getenv("SAVE_PATH")
COUNTRIES_JSON_DATA = os.getenv("COUNTRIES_JSON_DATA")
LOGGER_DJANGO = os.getenv("LOGGER_DJANGO")
TOKEN = os.environ.get("E5_BASE_V2_INFERENCE_ENDPOINT_TOKEN")
ENDPOINT_URL = os.environ.get("ENDPOINT_URL_E5_BASE_V2")
DATABASE_URL = os.getenv("READ_ONLY_DOADMIN_PUBLIC_NETWORK_POSTGRE_URL")

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


@retry(stop=stop_after_attempt(7), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(Exception), before_sleep=before_sleep_log(logger, logging.WARNING))
def extract_text_from_pdf(pdf_file):
	try:
		mime = magic.Magic(mime=True)
		mime_type = mime.from_buffer(pdf_file.read())
		if mime_type == 'application/pdf':
			pdf_file.seek(0)
			resource_manager = PDFResourceManager()
			text_stream = io.StringIO()
			device = TextConverter(resource_manager, text_stream)
			interpreter = PDFPageInterpreter(resource_manager, device)

			for page in PDFPage.get_pages(pdf_file):
				interpreter.process_page(page)

			extracted_text = text_stream.getvalue()
			device.close()
			text_stream.close()
			return extracted_text
		else:
			return None
	except Exception as e:
		logging.error(f"Exception at extract_text_from_pdf(). PDF was most likely not a valid pdf.\nException as follows: {e}.\n")
		return None
	



@retry(stop=stop_after_attempt(7), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(Exception), before_sleep=before_sleep_log(logger, logging.WARNING))
def DPO_actividades(extracted_text: str) -> list:
	url = "https://api.together.xyz/v1/chat/completions"

	payload = {
		"model": "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
		"max_tokens": 2000,
		"stop": [
		"<|im_end|>",
		"<|im_start|>"
		],
		"temperature": 0.1,
		"request_type": "language-model-inference",
		"top_p": 0.7,
		"top_k": 30,
		"n": 1,
		"messages": [
			{
				"role": "system",
				"content": f"{sugerir_actividades}===={extracted_text}===="
			}
		]
	}
	headers = {
		"accept": "application/json",
		"content-type": "application/json",
		"Authorization": f"Bearer {TOGETHER_API_KEY}"
	}

	response = requests.post(url, json=payload, headers=headers)

	response_data = json.loads(response.text)

	content = response_data['choices'][0]['message']['content']

	logging.info(content)

	parsed_list = ParseResponse(content)

	assert parsed_list is not None, "DPO_Extract_Skills() did not output a list."

	return parsed_list

def ParseResponse(response: str) -> list | None:
	list_str = re.findall(r'\[.*?\]', response, re.DOTALL)

	# Check if a list pattern was found
	if list_str:
		# Since findall returns a list of matches, we take the first match
		list_str = list_str[0]
		
		# Safely evaluate the string pattern to a Python list
		extracted_list = ast.literal_eval(list_str)
		return extracted_list
	else:
		return None

@retry(stop=stop_after_attempt(7), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(Exception), before_sleep=before_sleep_log(logger, logging.WARNING))
def RecomendacionActividadesGPT4(
	diagnostico: str,
) -> pd.DataFrame:
	
	
	logging.info(f"""\nCALLING: "gpt-4-1106-preview" """)

	client = OpenAI(
		api_key=OPENAI_API_KEY,
	)


	response = client.chat.completions.create(
		messages = [
			{"role": "system", "content": sugerir_actividades},
			{"role": "user", "content": f"####{diagnostico}####"}
		],
		
		model="gpt-4-1106-preview",
		temperature=0,
	)
	
	response_message = response.choices[0].message.content

	logging.info(f"gpt_4_response:\n\n{response_message}")

	parsed_list = ParseResponse(response_message)

	assert parsed_list is not None, "RecomendacionActividadesGPT4() did not output a list."

	return parsed_list

