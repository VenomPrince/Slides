import streamlit as st
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Laundry Monitor Demo",
    page_icon="🧺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to improve the look
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem !important;
        color: #1E88E5 !important;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem !important;
        color: #333 !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
    }
    .info-text {
        font-size: 1.2rem !important;
    }
    .highlight {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin-bottom: 1rem;
    }
    .status-running {
        color: #2E7D32 !important;
        font-weight: bold;
        font-size: 1.5rem !important;
    }
    .status-stopped {
        color: #C62828 !important;
        font-weight: bold;
        font-size: 1.5rem !important;
    }
    .code-block {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 5px;
        overflow-x: auto;
        margin-bottom: 1rem;
    }
    .stDataFrame {
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
    }
    .stMetric {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Create navigation sidebar
st.sidebar.markdown("# Navigation")
pages = [
    "Introduction",
    "How It Works",
    "Hardware Setup",
    "Software Code",
    "Live Demo",
    "Data Analysis",
    "Benefits & Applications",
    "Future Improvements"
]

selected_page = st.sidebar.radio("Go to", pages, label_visibility="collapsed")

# Add project info to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("## Project Info")
st.sidebar.markdown("**Creators:** Prince, Ashesh, and Nishant")
st.sidebar.markdown("**Date:** May 13, 2025")
st.sidebar.markdown("**Version:** 2.7")
st.sidebar.markdown("---")
st.sidebar.markdown("### Controls")
simulate_running = st.sidebar.checkbox("Simulate Running Machine", value=False)

# Function to generate mock sensor data for the demo
def generate_sensor_data(is_running=False):
    if is_running:
        # When running: lower values with some fluctuation
        return random.randint(50, 400)
    else:
        # When stopped: higher values with some fluctuation
        return random.randint(600, 900)

# Function to create historical data for charts
def generate_historical_data():
    # Create a week of data with random running periods
    now = datetime.now()
    dates = []
    statuses = []
    durations = []
    
    for i in range(7):
        day = now - timedelta(days=i)
        # Add 1-3 running cycles per day
        cycles_per_day = random.randint(1, 3)
        
        for j in range(cycles_per_day):
            # Random time during the day
            hour = random.randint(7, 21)
            minute = random.randint(0, 59)
            timestamp = day.replace(hour=hour, minute=minute)
            
            # Duration between 30 and 90 minutes
            duration = random.randint(30, 90)
            
            dates.append(timestamp)
            statuses.append("Running")
            durations.append(duration)
    
    df = pd.DataFrame({
        'date': dates,
        'status': statuses,
        'duration_minutes': durations
    })
    
    df['day_of_week'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    
    return df

# The Introduction page
def show_introduction():
    st.markdown("<h1 class='main-header'>Laundry Monitor System</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("<p class='info-text'>A smart IoT solution to monitor your laundry machine status remotely</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### Key Features:")
            st.markdown("- 🌐 **WiFi Connected:** Access from any device on your network")
            st.markdown("- 📱 **Responsive Web Interface:** Check status from phone or computer")
            st.markdown("- 🔄 **Real-time Updates:** Get immediate status changes")
            st.markdown("- 📊 **Data Tracking:** Monitor your laundry habits")
            st.markdown("- 🛠️ **Easy Setup:** Simple Arduino-based system")
        
    with col2:
        # Create a simple image to represent the laundry monitor
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.add_patch(plt.Rectangle((0.2, 0.2), 0.6, 0.6, fill=True, color='lightblue'))
        ax.add_patch(plt.Circle((0.5, 0.5), 0.25, fill=True, color='white'))
        ax.add_patch(plt.Circle((0.5, 0.5), 0.2, fill=False, color='blue', linewidth=2))
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        st.pyplot(fig, use_container_width=True)
        
        st.markdown("<p style='text-align:center'>Laundry Monitor Device</p>", unsafe_allow_html=True)

# The How It Works page
def show_how_it_works():
    st.markdown("<h1 class='main-header'>How It Works</h1>", unsafe_allow_html=True)
    
    st.markdown("<p class='info-text'>The Laundry Monitor uses a simple yet effective approach to detect machine status:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Working Principle:")
            st.markdown("""
            1. **Vibration Detection**: An analog vibration sensor detects machine movements
            2. **Signal Processing**: Arduino reads and processes sensor data
            3. **Status Determination**: Machine status is determined based on vibration levels
            4. **Web Server**: Arduino hosts a local web server
            5. **User Interface**: Status displayed on responsive web page
            """)
    with col2:
        # Create a better flowchart using matplotlib
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Define the component colors and positions
        components = [
            {"name": "Vibration\nSensor", "x": 0.1, "y": 0.5, "width": 0.15, "height": 0.3, "color": "#FFC107"},
            {"name": "Arduino\nProcessor", "x": 0.35, "y": 0.5, "width": 0.15, "height": 0.3, "color": "#4CAF50"},
            {"name": "WiFi\nModule", "x": 0.6, "y": 0.5, "width": 0.15, "height": 0.3, "color": "#2196F3"},
            {"name": "User\nDevices", "x": 0.85, "y": 0.5, "width": 0.15, "height": 0.3, "color": "#9C27B0"}
        ]
        
        # Draw each component
        for comp in components:
            ax.add_patch(plt.Rectangle(
                (comp["x"], comp["y"]), 
                comp["width"], comp["height"], 
                fill=True, 
                color=comp["color"],
                alpha=0.7,
                linewidth=2,
                edgecolor='black'
            ))
            ax.text(
                comp["x"] + comp["width"]/2, 
                comp["y"] + comp["height"]/2, 
                comp["name"], 
                ha='center', 
                va='center',
                fontweight='bold'
            )
        
        # Draw arrows between components
        for i in range(len(components) - 1):
            x1 = components[i]["x"] + components[i]["width"]
            y1 = components[i]["y"] + components[i]["height"]/2
            x2 = components[i+1]["x"]
            y2 = components[i+1]["y"] + components[i+1]["height"]/2
            
            ax.annotate(
                "", 
                xy=(x2, y2), 
                xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle="->",
                    linewidth=2,
                    color='#333333'
                )
            )
        
        # Add labels for the data being passed
        labels = ["Vibration\nData", "Processed\nStatus", "Status\nUpdate"]
        for i, label in enumerate(labels):
            x1 = components[i]["x"] + components[i]["width"]
            x2 = components[i+1]["x"]
            y = components[i]["y"] + components[i]["height"]/2 + 0.15
            ax.text((x1 + x2)/2, y, label, ha='center', va='center', fontsize=9, style='italic')
        
        # Add visualization for the sensor data
        sensor_x = components[0]["x"] + components[0]["width"]/2
        sensor_y = components[0]["y"] - 0.15
        wave_x = np.linspace(sensor_x - 0.1, sensor_x + 0.1, 100)
        wave_y = 0.03 * np.sin(40 * wave_x) + sensor_y
        ax.plot(wave_x, wave_y, 'r-', linewidth=1.5)
        ax.text(sensor_x, sensor_y - 0.05, "Vibrations", ha='center', va='center', fontsize=8)
        
        # Add visualization for the WiFi signal
        wifi_x = components[2]["x"] + components[2]["width"]/2
        wifi_y = components[2]["y"] - 0.15
        
        # Draw WiFi arcs
        for i in range(3):
            radius = 0.03 + i * 0.02
            arc = plt.matplotlib.patches.Arc(
                (wifi_x, wifi_y), 
                radius*2, radius*2, 
                theta1=210, theta2=330, 
                linewidth=1.5,
                color='blue'
            )
            ax.add_patch(arc)
        
        # Draw the user's phone/tablet receiving data
        user_device_x = components[3]["x"] + components[3]["width"]/2
        user_device_y = components[3]["y"] - 0.15
        
        # Phone outline
        ax.add_patch(plt.Rectangle(
            (user_device_x - 0.04, user_device_y - 0.1), 
            0.08, 0.15, 
            fill=True, 
            color='lightgray',
            linewidth=1,
            edgecolor='black'
        ))
        
        # Phone screen
        ax.add_patch(plt.Rectangle(
            (user_device_x - 0.035, user_device_y - 0.09), 
            0.07, 0.12, 
            fill=True, 
            color='white',
            linewidth=1,
            edgecolor='black'
        ))
        
        # Status text on phone
        ax.text(
            user_device_x, 
            user_device_y - 0.03, 
            "Status:", 
            ha='center', 
            va='center', 
            fontsize=7
        )
        ax.text(
            user_device_x, 
            user_device_y - 0.06, 
            "Running", 
            ha='center', 
            va='center', 
            fontsize=7,
            color='green',
            fontweight='bold'
        )
        
        # Remove axes
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        st.pyplot(fig, use_container_width=True)
        
        with st.container(border=True):
            st.markdown("### Threshold-Based Detection:")
            st.markdown("""
            - Sensor reading **below threshold** → Machine is **Running** 🌀
            - Sensor reading **above threshold** → Machine is **Stopped** 🧺
            """)

# The Hardware Setup page
def show_hardware_setup():
    st.markdown("<h1 class='main-header'>Hardware Setup</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        with st.container(border=True):
            st.markdown("### Components Required:")
            st.markdown("""
            - Arduino Nano 33 IoT (or similar with WiFi)
            - Analog vibration sensor module
            - Breadboard
            - Jumper wires
            - USB power supply
            - Small enclosure (optional)
            """)
        
        st.markdown("### Connections:")
        st.markdown("""
        1. Connect vibration sensor VCC to Arduino 3.3V
        2. Connect vibration sensor GND to Arduino GND
        3. Connect vibration sensor OUT to Arduino A0
        4. Power Arduino via USB
        """)
    
    with col2:
        # Create a simple diagram of connections
        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Draw Arduino
        ax.add_patch(plt.Rectangle((0.1, 0.3), 0.3, 0.4, fill=True, color='lightblue'))
        ax.text(0.25, 0.5, "Arduino", ha='center', va='center')
        
        # Draw Sensor
        ax.add_patch(plt.Rectangle((0.6, 0.3), 0.3, 0.4, fill=True, color='lightgreen'))
        ax.text(0.75, 0.5, "Sensor", ha='center', va='center')
        
        # Draw connection lines
        ax.plot([0.4, 0.6], [0.4, 0.4], 'r-', linewidth=2)
        ax.text(0.5, 0.42, "A0", ha='center', va='bottom', color='red')
        
        ax.plot([0.4, 0.6], [0.5, 0.5], 'k-', linewidth=2)
        ax.text(0.5, 0.52, "GND", ha='center', va='bottom')
        
        ax.plot([0.4, 0.6], [0.6, 0.6], 'b-', linewidth=2)
        ax.text(0.5, 0.62, "3.3V", ha='center', va='bottom', color='blue')
        
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        st.pyplot(fig, use_container_width=True)
        
        with st.container(border=True):
            st.markdown("### Installation Tips:")
            st.markdown("""
            - Place the sensor securely on the laundry machine
            - Find an optimal position that detects vibrations clearly
            - Keep electronics away from water/moisture
            - Use double-sided tape or mounting bracket
            """)

# The Software Code page
def show_software_code():
    st.markdown("<h1 class='main-header'>Software Code</h1>", unsafe_allow_html=True)
    
    st.markdown("### Arduino Sketch")
    
    with st.container(border=True):
        st.code("""
#include <WiFiNINA.h>
const char ssid[] = "Laundry_AP";
const char pass[] = "laundry123";
WiFiServer server(80);
const int sensorPin = A0;
const int threshold = 500; // we can adjust this if needed
String lastStatus = "Unknown"; // to track status changes

void setup() {
  Serial.begin(9600); // for debugging
  while (!Serial); // wait for serial port to open
  pinMode(sensorPin, INPUT); // set sensor pin as input
  WiFi.beginAP(ssid, pass); // start access point
  delay(1000);
  server.begin();
  Serial.println("Access Point Started");
  Serial.println("Connect to: http://192.168.4.1");
}

String getStatus() {
  int val = analogRead(sensorPin);
  Serial.print("Sensor value: ");
  Serial.println(val);
  // Invert logic: LOW value means vibration (Running), HIGH means no vibration (Stopped)
  return (val < threshold) ? "Running 🌀" : "Stopped 🧺"; 
}

void sendWebPage(WiFiClient client) { // send HTML page
  client.println("HTTP/1.1 200 OK"); // send HTTP header
  client.println("Content-Type: text/html");
  client.println("Connection: close"); // close connection
  client.println();
  client.println(R"rawliteral( // HTML content
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Laundry Monitor</title>
  <style>
    body { font-family: Arial; background: #f9f9f9; text-align: center; padding-top: 50px; }
    h1 { color: #333; }
    .status { font-size: 2em; margin-top: 20px; color: #222; }
  </style>
</head>
<body>
  <h1>Laundry Status Monitor 🧼</h1>
  <div class="status">Status: <span id="stat">Loading...</span></div>
  <script>
    async function update() {
      const res = await fetch('/status');
      const data = await res.json();
      document.getElementById('stat').innerText = data.status;
    }
    update();
    setInterval(update, 2000);
  </script>
</body>
</html>
)rawliteral");
}

void sendStatusJSON(WiFiClient client) {
  client.println("HTTP/1.1 200 OK"); // send HTTP header
  client.println("Content-Type: application/json");
  client.println("Connection: close");
  client.println();
  client.print("{\"status\":\""); // send JSON response
  client.print(lastStatus);
  client.println("\"}");
}

void loop() {
  String currentStatus = getStatus();
  if (currentStatus != lastStatus) {
    lastStatus = currentStatus;
    Serial.println("Status changed: " + currentStatus);
  }
  WiFiClient client = server.available();
  if (client) {
    String req = client.readStringUntil('\\r');
    client.flush();
    if (req.indexOf("GET /status") >= 0) {
      sendStatusJSON(client);
    } else {
      sendWebPage(client);
    }
    delay(1);
    client.stop();
  }
  delay(300);
}
        """, language="cpp")
    
    st.markdown("### Code Explanation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("#### Key Components:")
            st.markdown("""
            - **WiFi Access Point:** Creates network "Laundry_AP"
            - **Web Server:** Hosts interface on 192.168.4.1
            - **Sensor Reading:** Monitors analog pin A0
            - **Status Logic:** Below 500 = Running, Above = Stopped
            - **Web Interface:** Responsive HTML page with auto-refresh
            - **API Endpoint:** JSON response at /status
            """)
    
    with col2:
        st.markdown("#### How to Customize:")
        st.markdown("""
        - Adjust `threshold` value based on your sensor's sensitivity
        - Modify `ssid` and `pass` for your preferred network name and password
        - Customize the HTML interface design
        - Add features like:
          - Notifications when status changes
          - Historical logging
          - Multiple machine support
        """)

# The Live Demo page
def show_live_demo():
    st.markdown("<h1 class='main-header'>Live Demo</h1>", unsafe_allow_html=True)
    
    # Get the simulation state from sidebar
    is_running = simulate_running
    
    # Generate a sensor value based on current state
    sensor_value = generate_sensor_data(is_running)
    status = "Running 🌀" if sensor_value < 500 else "Stopped 🧺"
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create a mock web interface similar to the Arduino one
        with st.container(border=True):
            st.markdown("<h2 style='text-align:center'>Laundry Status Monitor 🧼</h2>", unsafe_allow_html=True)
            
            if status == "Running 🌀":
                st.markdown(f"<div style='text-align:center'>Status: <span class='status-running'>{status}</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align:center'>Status: <span class='status-stopped'>{status}</span></div>", unsafe_allow_html=True)
                
            st.markdown("<p style='margin-top: 20px; color: #666; text-align:center'>Last updated: Just now</p>", unsafe_allow_html=True)
    
    with col2:
        with st.container(border=True):
            st.markdown("### Live Sensor Data:")
            st.metric("Vibration Level", sensor_value, delta=None)
            st.markdown(f"Threshold: 500 (Configured)")
    
    # Create a real-time chart
    st.markdown("<h3 class='sub-header'>Real-time Sensor Readings</h3>", unsafe_allow_html=True)
    
    # Simulate historical data for the chart
    chart_data = pd.DataFrame({
        'time': list(range(30)),
        'value': [generate_sensor_data(is_running if i > 15 else not is_running) for i in range(30)]
    })
    
    # Add threshold line
    threshold_df = pd.DataFrame({
        'time': [0, 29],
        'threshold': [500, 500]
    })
    
    # Create chart
    chart = alt.Chart(chart_data).mark_line(color='#1E88E5').encode(
        x=alt.X('time', title='Time (seconds ago)'),
        y=alt.Y('value', title='Sensor Value', scale=alt.Scale(domain=[0, 1000]))
    )
    
    threshold_line = alt.Chart(threshold_df).mark_line(color='red', strokeDash=[3, 3]).encode(
        x='time',
        y='threshold'
    )
    
    st.altair_chart((chart + threshold_line).properties(height=300), use_container_width=True)
    
    # Add a placeholder for real-time updates (in a real app, this would update)
    status_placeholder = st.empty()
    
    # Auto-refresh section
    st.markdown("<div style='display: flex; justify-content: center; margin-top: 20px;'>", unsafe_allow_html=True)
    if st.button("Refresh Data"):
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Note about demo
    st.markdown("""
    > **Note:** In a real implementation, the web interface would automatically update every few seconds.
    > Use the "Simulate Running Machine" checkbox in the sidebar to change the simulated status.
    """)

# The Data Analysis page
def show_data_analysis():
    st.markdown("<h1 class='main-header'>Data Analysis</h1>", unsafe_allow_html=True)
    
    # Generate mock historical data
    df = generate_historical_data()
    
    st.markdown("<p class='info-text'>With collected data over time, we can analyze laundry usage patterns:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 class='sub-header'>Usage by Day of Week</h3>", unsafe_allow_html=True)
        
        day_counts = df.groupby('day_of_week').size().reset_index(name='count')
        # Reorder days correctly
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_counts['day_of_week'] = pd.Categorical(day_counts['day_of_week'], categories=days_order, ordered=True)
        day_counts = day_counts.sort_values('day_of_week')
        
        chart = alt.Chart(day_counts).mark_bar().encode(
            x=alt.X('day_of_week', title='Day of Week'),
            y=alt.Y('count', title='Number of Cycles'),
            color=alt.Color('day_of_week', legend=None, scale=alt.Scale(scheme='blues'))
        )
        
        st.altair_chart(chart, use_container_width=True)
    
    with col2:
        st.markdown("<h3 class='sub-header'>Usage by Time of Day</h3>", unsafe_allow_html=True)
        
        hour_counts = df.groupby('hour').size().reset_index(name='count')
        
        chart = alt.Chart(hour_counts).mark_line(point=True).encode(
            x=alt.X('hour', title='Hour of Day', scale=alt.Scale(domain=[0, 23])),
            y=alt.Y('count', title='Number of Starts'),
            tooltip=['hour', 'count']
        )
        
        st.altair_chart(chart, use_container_width=True)
    
    # Cycle duration analysis
    st.markdown("<h3 class='sub-header'>Cycle Duration Analysis</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        with st.container(border=True):
            st.markdown("### Statistics:")
            st.markdown(f"**Average Duration:** {df['duration_minutes'].mean():.1f} minutes")
            st.markdown(f"**Shortest Cycle:** {df['duration_minutes'].min()} minutes")
            st.markdown(f"**Longest Cycle:** {df['duration_minutes'].max()} minutes")
            st.markdown(f"**Total Cycles:** {len(df)}")
            st.markdown(f"**Total Machine Time:** {df['duration_minutes'].sum() / 60:.1f} hours")
    
    with col2:
        # Duration histogram
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('duration_minutes', bin=alt.Bin(maxbins=10), title='Duration (minutes)'),
            y=alt.Y('count()', title='Number of Cycles')
        )
        
        st.altair_chart(chart, use_container_width=True)

# The Benefits & Applications page
def show_benefits():
    st.markdown("<h1 class='main-header'>Benefits & Applications</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Key Benefits:")
            st.markdown("""
            - ⏱️ **Time Saving:** No need to physically check machine status
            - 🏠 **Convenient:** Check from anywhere in your home
            - 📈 **Efficiency:** Plan around laundry completion
            - 🔔 **Peace of Mind:** Know exactly when cycle finishes
            - 💡 **Energy Awareness:** Track usage patterns
            """)
    
    with col2:
        st.markdown("### Ideal For:")
        st.markdown("""
        - 🏢 **Shared Laundry Facilities** in apartments or dorms
        - 🏠 **Multi-level Homes** where laundry room is far away
        - 👨‍👩‍👧‍👦 **Busy Families** juggling multiple responsibilities
        - 👨‍💻 **Remote Workers** who need to multitask
        - 👵 **Elderly or Mobility-Limited** individuals
        """)
    
    st.markdown("<h3 class='sub-header'>Implementation Ideas</h3>", unsafe_allow_html=True)
    
    ideas = pd.DataFrame({
        'Application': [
            'Home Automation Integration', 
            'Mobile App Notifications', 
            'Multi-Machine Monitoring',
            'Usage Analytics Dashboard',
            'Voice Assistant Integration'
        ],
        'Description': [
            'Connect with home automation systems like Home Assistant or SmartThings',
            'Send push notifications when laundry cycle completes',
            'Expand to monitor washer and dryer simultaneously',
            'Track usage patterns and provide insights on optimal laundry times',
            'Ask Alexa or Google Home about laundry status'
        ],
        'Complexity': [
            'Medium', 
            'Medium', 
            'Easy', 
            'Medium', 
            'Hard'
        ]
    })
    
    st.dataframe(ideas, use_container_width=True, hide_index=True)

# The Future Improvements page
def show_future_improvements():
    st.markdown("<h1 class='main-header'>Future Improvements</h1>", unsafe_allow_html=True)
    
    st.markdown("<p class='info-text'>The project has several potential enhancement paths:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Hardware Enhancements:")
            st.markdown("""
            - 🔋 **Battery Power Option** for cable-free installation
            - 📶 **ESP32 Upgrade** for Bluetooth + WiFi capabilities
            - 🔊 **Sound Detection** as an additional sensing method
            - 📱 **Standalone Display** for at-a-glance status
            - 🔌 **Energy Monitoring** to track power consumption
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("### Software Improvements:")
            st.markdown("""
            - 🌐 **Cloud Integration** for remote access
            - 📊 **Advanced Analytics** for deeper usage insights
            - 🔔 **Push Notifications** for cycle completion alerts
            - 🔄 **Machine Learning** to improve detection accuracy
            - 🗓️ **Scheduling Features** to plan laundry times
            """)
    
    st.markdown("<h3 class='sub-header'>Development Roadmap</h3>", unsafe_allow_html=True)
    
    roadmap_data = pd.DataFrame({
        'Phase': ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
        'Task': [
            'Basic Vibration Detection & Web Interface',
            'Add Data Logging & Notifications',
            'Cloud Integration & Mobile App',
            'Multi-device Support & Analytics'
        ],
        'Status': ['✅ Completed', '🔄 In Progress', '📅 Planned', '🔮 Future']
    })
    
    st.dataframe(
        roadmap_data,
        column_config={
            "Status": st.column_config.SelectboxColumn(
                "Status",
                options=["✅ Completed", "🔄 In Progress", "📅 Planned", "🔮 Future"],
                required=True,
                default="📅 Planned"
            )
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.markdown("<h3 class='sub-header'>Community & Support</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    This project is open-source and welcomes contributions!

    - 📁 **GitHub Repository:** [github.com/VenomPrince/laundry-monitor](https://github.com/VenomPrince/laundry-monitor)
    - 🤝 **Community Forum:** Share your implementations and ideas
    - 📚 **Documentation:** Full setup guide and API documentation available
    - 🐞 **Issue Tracking:** Report bugs and feature requests
    """)

# Display the selected page
if selected_page == "Introduction":
    show_introduction()
elif selected_page == "How It Works":
    show_how_it_works()
elif selected_page == "Hardware Setup":
    show_hardware_setup()
elif selected_page == "Software Code":
    show_software_code()
elif selected_page == "Live Demo":
    show_live_demo()
elif selected_page == "Data Analysis":
    show_data_analysis()
elif selected_page == "Benefits & Applications":
    show_benefits()
elif selected_page == "Future Improvements":
    show_future_improvements()

# Add footer
st.markdown("---")
st.markdown("<p style='text-align:center'>Laundry Monitor <3 by VenomPrince, Ashes and Nishant</p>", unsafe_allow_html=True)