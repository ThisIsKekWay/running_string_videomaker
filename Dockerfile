FROM python:3.9

RUN mkdir /videomaker

WORKDIR /videomaker

RUN mkdir /videomaker/media

RUN apt-get update && apt-get install -y \
    python3-opencv \
    libsm6 \
    libgl1-mesa-glx \
    libxkbcommon-x11-0 \
    libxcb-cursor0 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxcb1 \
    libxrender1 \
    libxi6 \
    libdbus-1-3 \
    libxcb* \
    libegl1

COPY reqs.txt .

RUN pip install --upgrade pip

RUN pip install -r reqs.txt

COPY . .