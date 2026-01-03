# 🕵️‍♂️ Web Privacy Analyzer

**Deep-Dive Browser Fingerprinting & Leak Detection**

A lightweight, privacy-first forensic tool that exposes exactly what your browser reveals to the web. From HTTP headers to WebGL hardware leaks, see your digital footprint in real-time.

---

### Features • [Installation](#-installation) • [Architecture](#-architecture) • [Privacy](#%EF%B8%8F-privacy-architecture)

---

## 👁️ What is Web Privacy Analyzer?

**Web Privacy Analyzer** is a forensic dashboard designed for security researchers and privacy-conscious users. Unlike standard "what is my IP" sites, this tool performs a dual-layer analysis:

1.  **Server-Side Interception**: Captures raw HTTP request headers, proxy forwarded IPs, and protocol metadata.
2.  **Client-Side Fingerprinting**: Executes JavaScript probes to extract hardware details, screen metrics, and WebGL renderer info that can uniquely identify users even behind a VPN.

It runs entirely in **Volatile Memory Mode**—no logs, no databases, no traces left behind.

## 🔑 Key Highlights

| Feature | Description |
| :--- | :--- |
| **💀 Zero-Log Policy** | Flask logs are explicitly disabled. IPs are never written to disk. |
| **🖥️ Hardware Leaks** | Extracts GPU Vendor & Renderer strings via WebGL to identify your exact graphics card. |
| **🕵️ Header Forensics** | Inspects `Sec-Ch-Ua` and `X-Forwarded-For` to detect proxies and platform spoofing. |
| **🧩 Fingerprinting** | Calculates screen resolution, color depth, and timezone offsets to generate a unique browser ID. |
| **🚫 DNT Detection** | Verifies if your browser's "Do Not Track" signal is actually being broadcast. |

## 🛠️ The Analysis Modules

### 1. Network Layer (Server-Side)
Directly inspects the incoming HTTP packet to reveal:
*   **True IP Address**: Bypasses simple proxies via `X-Forwarded-For`.
*   **Protocol Headers**: `User-Agent`, `Referer`, `Host`, and `Connection` types.
*   **Sec-CH-UA**: Analysis of the new Client Hints standard used by modern browsers.

### 2. Fingerprint Layer (Client-Side)
Deploys JavaScript probes to extract local system data:
*   **WebGL Hardware**: Identifies the Unmasked Vendor and Renderer (e.g., "NVIDIA GeForce RTX 3080").
*   **System Metrics**: Screen resolution, Color Depth (bits), and System Timezone.
*   **Cookie Status**: Instant check for cookie storage availability.

## 🚀 Installation

### Prerequisites
*   Python 3.x
*   Flask

### 1️⃣ Clone & Install
```bash
git clone https://github.com/rajasronghe/web-privacy-analyzer.git
cd web-privacy-analyzer
pip install flask
```

### 2️⃣ Launch the Analyzer
Start the server in debug mode (default port 5000):
```bash
python3 privacy_analyzer/app.py
```
> **Note**: The application is configured to suppress standard access logs for privacy.

### 3️⃣ Access Dashboard
Open your web browser and navigate to: [http://localhost:5000](http://localhost:5000)

## 🎨 Interface

The dashboard features a **Cyber-Forensic UI** (Green-on-Black) for high contrast and readability.

```text
Privacy Analyzer
See what data is exposed from your browser.

[1. Network & Request Headers]
--------------------------------------------------
Public IP Address:   192.168.1.50
User-Agent:          Mozilla/5.0 (Windows NT 10.0...
Platform (OS):       "Windows"
Do Not Track (DNT):  Disabled

[2. Browser Fingerprint]
--------------------------------------------------
Screen Resolution:   2560x1440
Color Depth:         24-bit
Timezone:            America/New_York

[3. WebGL Hardware]
--------------------------------------------------
WebGL Vendor:        Google Inc. (NVIDIA)
WebGL Renderer:      ANGLE (NVIDIA, NVIDIA GeForce RTX 3080...
```

## ⚠️ Privacy Architecture

This tool was built with a **"Privacy-First"** architecture:

*   **Volatile Memory**: Data is reflected back to the user immediately and discarded.
*   **Log Suppression**: The application explicitly disables the `werkzeug` logger to prevent writing IP addresses to the server console.
*   **No Persistence**: No database, no cookies, no tracking pixels.