from typing import Union

from pydantic import BaseModel


class TextData(BaseModel):
    texts: list


def prob_to_severity(prob: float) -> Union[int, None]:
    if 0.8 < prob <= 1.0:
        return 0
    elif 0.5 < prob <= 0.8:
        return 1
    else:
        return None
