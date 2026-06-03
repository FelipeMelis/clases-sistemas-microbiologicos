# Setup Instructions

**Before the first class (required):** complete steps 1, 2, and 3 (Miniforge3 + clone repo + QIIME2). The QIIME2 download is large (~5GB) and takes 20–40 minutes. Windows users: complete steps 1, 2, 3, and 4.

**Before Módulo 2 (can wait):** step 4 (PyDESeq2) for Mac / step 5 (PyDESeq2) for Windows — quick and can be done right before that session.

---

## Mac

### 1. Install Miniforge3 (includes mamba)

First, check what kind of Mac you have: Apple menu → About This Mac.
- **Apple Silicon (M1/M2/M3/M4):** use the `arm64` installer
- **Intel Mac:** use the `x86_64` installer

**Apple Silicon:**
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"
bash Miniforge3-MacOSX-arm64.sh
```

**Intel Mac:**
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh"
bash Miniforge3-MacOSX-x86_64.sh
```

Follow the prompts, accept the license, and let it initialize. Then restart your terminal and verify:
```bash
mamba --version
```

---

### 2. Clone the class repo

```bash
cd ~
git clone https://github.com/FelipeMelis/clases-sistemas-microbiologicos.git
cd clases-sistemas-microbiologicos
```

> Keep this terminal open for the next steps — they assume you are inside this folder.

---

### 3. Install QIIME2 (Módulo 1)

> QIIME2 on Apple Silicon runs in Rosetta 2 emulation mode — this is expected and works correctly.

**Apple Silicon:**
```bash
curl -sL "https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2025.4-py310-osx-conda.yml" -o qiime2-env.yml
CONDA_SUBDIR=osx-64 mamba env create -n qiime2-amplicon-2025.4 -f qiime2-env.yml
conda activate qiime2-amplicon-2025.4
conda config --env --set subdir osx-64
```

**Intel Mac:**
```bash
curl -sL "https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2025.4-py310-osx-conda.yml" -o qiime2-env.yml
mamba env create -n qiime2-amplicon-2025.4 -f qiime2-env.yml
conda activate qiime2-amplicon-2025.4
```

Verify:
```bash
qiime --version
```

---

### 4. Install PyDESeq2 dependencies (Módulo 2)

Make sure you are in the repo folder and in the base environment:
```bash
cd ~/clases-sistemas-microbiologicos
conda activate base
pip install -r environment/requirements_pydeseq2.txt
```

---

## Windows

Windows requires **WSL2** (Windows Subsystem for Linux) to run QIIME2. This is a one-time setup.

### 1. Install WSL2

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

This installs WSL2 with Ubuntu. Restart your computer when prompted.

After restarting, open **Ubuntu** from the Start menu and create a username and password when asked.

Verify WSL2 is working:
```bash
uname -a
# Should show something like: Linux ... x86_64 GNU/Linux
```

### 2. Install Miniforge3 inside WSL2 (includes mamba)

Inside the Ubuntu terminal:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh
```

Follow the prompts and let it initialize. Then restart the terminal and verify:
```bash
mamba --version
```

### 3. Clone the class repo inside WSL2

```bash
cd ~
git clone https://github.com/FelipeMelis/clases-sistemas-microbiologicos.git
cd clases-sistemas-microbiologicos
```

> Keep this terminal open for the next steps — they assume you are inside this folder.

### 4. Install QIIME2 (Módulo 1)

```bash
curl -sL "https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2025.4-py310-linux-conda.yml" -o qiime2-env.yml
mamba env create -n qiime2-amplicon-2025.4 -f qiime2-env.yml
conda activate qiime2-amplicon-2025.4
```

Verify:
```bash
qiime --version
```

### 5. Install PyDESeq2 dependencies (Módulo 2)

Make sure you are in the repo folder and in the base environment:
```bash
cd ~/clases-sistemas-microbiologicos
conda activate base
pip install -r environment/requirements_pydeseq2.txt
```

### 6. Open Jupyter notebooks from WSL2

Activate the QIIME2 environment first, then launch Jupyter:
```bash
conda activate qiime2-amplicon-2025.4
jupyter notebook
```

Copy the URL that appears (starting with `http://127.0.0.1:8888/...`) and paste it into your Windows browser.

---

## Verify everything is working

```bash
# QIIME2
conda activate qiime2-amplicon-2025.4
qiime --version
jupyter notebook --version

# PyDESeq2 — run from base environment
conda activate base
python -c "import pydeseq2; print('PyDESeq2 OK')"
```

---

## Troubleshooting

**`qiime: command not found` after activating the environment** — If you have Anaconda already installed, `conda activate` may look in the wrong place. Use the full path instead:
```bash
conda activate ~/miniforge3/envs/qiime2-amplicon-2025.4
```

**`mamba: command not found`** — Close and reopen the terminal, then try again. If it persists, run `source ~/.bashrc`.

**WSL2 install fails on Windows** — Make sure virtualization is enabled in your BIOS. Search "enable virtualization Windows 11" for your specific laptop model.

**QIIME2 install is very slow** — Normal. The environment is ~5GB. Let it run and do not interrupt it.

**Jupyter does not open on Windows** — Make sure you are copying the full URL including the token from the WSL2 terminal output.

If you are still stuck, bring your laptop to the Módulo 3 session.
