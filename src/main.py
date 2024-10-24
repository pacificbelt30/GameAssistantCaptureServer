from typing import Tuple
import os
import io
# import pyautogui
from fastapi import FastAPI, Response


async def capture_screen(initial_point: Tuple[int, int]=(0, 0), width: int=600, height: int=600) -> io.BytesIO:
    # 特定の領域をスクリーンショットとして撮影
    screenshot = await pyautogui.screenshot(region=(*initial_point, width, height))
    output = io.BytesIO()
    await screenshot.save(output)

    return output

app = FastAPI()

@app.get('/')
async def main():
    return 'This is Windows Screen Capture Server'

@app.get('/capture')
async def plot_png():
    png = await capture_screen()
    # 画像ファイルをクライアントに送信
    png.seek(0)
    return Response(content=png, media_type="/image/png")
