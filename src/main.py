from typing import Tuple
import os
import io
import base64
import pyautogui
from fastapi import FastAPI, Response


def capture_screen(initial_point: Tuple[int, int]=(0, 0), width: int=600, height: int=600) -> str:
    # 特定の領域をスクリーンショットとして撮影
    screenshot = pyautogui.screenshot(region=(*initial_point, width, height))
    output = io.BytesIO()
    screenshot.save(output)
    output.seek(0)
    b64 = base64.b64encode(output.read())

    return b64.decode('utf-8')

app = FastAPI()

@app.get('/')
async def main():
    return 'This is Windows Screen Capture Server'

@app.get('/capture')
async def plot_png(init_x:int = 0, init_y:int = 0, width:int = 600, height:int = 600):
    png = capture_screen((init_x, init_y), width, height)
    output = {'img': 'data:image/png;base64,'+png}
    # 画像ファイルをクライアントに送信
    return output
