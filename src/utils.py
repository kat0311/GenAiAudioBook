

from httpx import Timeout
from langchain_openai import AzureChatOpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


class GPTModels:
    # GPT_4o = "gpt-4o"
    # GPT_4o_MINI = "gpt-4o-mini"
    # GPT_4_TURBO_2024_04_09 = "gpt-4-turbo-2024-04-09"
    GPT_4 = "gpt-4o" 



def get_chat_llm(llm_model: GPTModels, temperature=0.0):
    llm = AzureChatOpenAI(openai_api_version="2023-05-15", 
                        azure_deployment="gpt-4o",temperature=0)
    return llm


async def consume_aiter(aiterator):
    return [x async for x in aiterator]


def auto_retry(f):
    decorator = retry(
        wait=wait_random_exponential(min=2, max=6),
        stop=stop_after_attempt(10),
    )
    return decorator(f)
