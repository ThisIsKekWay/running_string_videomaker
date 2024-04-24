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
    libegl1\
    libegl1-mesa-dev\
    libvncserver-dev\
    libx11-dev\
    libgbm-dev\
    libvulkan-dev\
    libxcb-xinerama0-dev \
    libxcb-xkb-dev \
    libxcb-xtest0-dev \
    libxcb-cursor-dev \
    libxcb-shape0-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-xfixes0-dev \
    libxcb-sync-dev \
    libxcb-xinput-dev \
    libxcb-xinerama0-dev \
    libxcb-xkb-dev \
    libxcb-xtest0-dev \
    libxcb-cursor-dev \
    libxcb-shape0-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-xfixes0-dev \
    libxcb-sync-dev \
    libxcb-xinput-dev

COPY reqs.txt .

RUN pip install --upgrade pip

RUN pip install -r reqs.txt

COPY . .