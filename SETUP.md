# Setup Instructions

Follow these steps **before the first class**. The full installation takes 20–40 minutes depending on your internet connection.

---

## Mac

### 1. Install Miniforge3 (includes mamba)

Download and run the installer:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"
bash Miniforge3-MacOSX-arm64.sh
```

> If you have an older Intel Mac, replace `arm64` with `x86_64` in the filename.

Follow the prompts, accept the license, and let it initialize. Then restart your terminal.

Verify it works:
```bash
mamba --version
```

---

### 2. Install QIIME2 (Módulo 1)

```bash
mamba env create -f environment/environment_qiime2.yml
conda activate qiime2-amplicon-2024.10
```

Verify:
```bash
qiime --version
```

---

### 3. Install PyDESeq2 dependencies (Módulo 2)

```bash
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

### 4. Install QIIME2 (Módulo 1)

```bash
mamba env create -f environment/environment_qiime2.yml
conda activate qiime2-amplicon-2024.10
```

Verify:
```bash
qiime --version
```

### 5. Install PyDESeq2 dependencies (Módulo 2)

```bash
pip install -r environment/requirements_pydeseq2.txt
```

### 6. Open Jupyter notebooks from WSL2

Inside WSL2, run:
```bash
jupyter notebook
```

Copy the URL that appears (starting with `http://127.0.0.1:8888/...`) and paste it into your Windows browser.

---

## Verify everything is working

Run this after setup to confirm both environments are ready:

```bash
# QIIME2
conda activate qiime2-amplicon-2024.10
qiime --version
jupyter notebook --version

# PyDESeq2
python -c "import pydeseq2; print('PyDESeq2 OK')"
```

---

## Troubleshooting

**`mamba: command not found`** — Close and reopen the terminal, then try again. If it persists, run `source ~/.bashrc`.

**WSL2 install fails on Windows** — Make sure virtualization is enabled in your BIOS. Search "enable virtualization Windows 11" for your specific laptop model.

**QIIME2 install is very slow** — Normal. The environment is ~5GB. Let it run and do not interrupt it.

**Jupyter does not open on Windows** — Make sure you are copying the full URL including the token from the WSL2 terminal output.

If you are still stuck, bring your laptop to the Módulo 3 session.
