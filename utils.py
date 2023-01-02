from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from functools import wraps
import time
import logger

def retry(function):
    RETRIES_LIMIT = 3
    loger_ = logger.create_logger()
    @wraps(function)
    async def wraaped(self, **kwargs):
        for _ in range(RETRIES_LIMIT):
            try:
                return await function(self, **kwargs) if kwargs else await function(self)
            
            except PlaywrightTimeoutError: #element를 못찾는 경우
                loger_.warn((f"Retry function: {function}"))
                if 'timeout' in kwargs:
                    kwargs['timeout'] += 2000
                continue

            except AssertionError:
                continue
        
        #최대 반복횟수를 도달했지만 함수가 반환이 안되면 예외이다.
        raise Exception(f"{function} occurs error!")

    return wraaped


def parse_grade(inner_texts:str):
    column_names = ['이수학년도','이수학기','과목코드','과목명','과목학점','성적','등급','교수명','비고']
    column_len = len(column_names)
    table_texts = inner_texts.split('\t')
    text_by_rows = [table_texts[i:i + len(column_names)] for i in range(column_len + 2, len(table_texts), column_len + 1)]
    grade_info = [{col:value for col, value in zip(column_names,row)} for row in text_by_rows]
    return grade_info
