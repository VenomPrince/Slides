# Slides for Project: ATmega328PB, Arduino MKR WiFi 1010, and Vibration Sensor 2.0

This project demonstrates an embedded system setup using:
- **ATmega328PB** for vibration detection
- **Arduino MKR WiFi 1010** for web interface and WiFi communication
- **Vibration Sensor 2.0** for monitoring motion (e.g., washing machine status)
- **Streamlit** for interactive presentation of the project

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/VenomPrince/Slides
cd Slides
```

### 2. Run the Setup Script

Execute the provided script to:

- Automatically create a Python virtual environment
- Install required dependencies from `requirements.txt`
- Launch the Streamlit web app

```bash
./runreq.sh
```

> ⚠️ If you get a permission denied error, give the script execute permissions:

```bash
chmod +x runreq.sh
```

### 3. View the Slides

Once the app starts, Streamlit will provide a link like:

```
Local URL: http://localhost:8501
```

Click the link or paste it into your browser to view the slides.

---

## Requirements

All required Python packages are listed in `requirements.txt`:

```
streamlit
pandas
matplotlib
altair
```

They are automatically installed when you run:

```bash
./runreq.sh
```

---

## 🛠️ Notes

- Compatible with Linux and macOS terminals
- Tested with Python 3.8 and above
- Make sure you have `python3` installed

---
