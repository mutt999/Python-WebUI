# Embedded Web UI

A modern embedded web interface combining a Python-based backend with a fast, responsive frontend built using Vue.js and TypeScript.  
The backend and frontend communicate seamlessly through a lightweight JSON-RPC interface, ensuring efficient data exchange and a clean architectural separation.
---

## 🚀 Requirements

- **Python 3** installed
- **Node.js with npm** installed
- (Optional) A terminal/command prompt to run the setup scripts

---

## 🔧 Installation & Setup

This project uses a Python virtual environment along with a list of required modules to set up the environment automatically.

### 1. Create a Python virtual environment

```bash
call app_env_create.bat
```

### 2. Install required Python modules

```bash
call app_env_restore.bat
```

### 3. Build web part

```bash
call web_build.bat
```

### 4. Start the application

```bash
call app_main_ui.bat
```
