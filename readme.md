# Mapping with the HC-SR04 sensor
This project aims to mimic LiDAR's mapping functionality using just a servo motor and an ultrasonic distance sensor (HC-SR04). 

### Physical configuration
The distance sensor is mounted atop a servo motor. Both are controlled by an Arduino Uno. Two pushbuttons on a breadboard control measurement sweeps. The circuit setup is described in [Circuit diagram.png](Circuit%20diagram.png). 

The Arduino is used to rotate the servo, and consequently the sensor, in fixed intervals. The servo's $0\degree$ is aligned with the positive x-axis and its heading is thus $90\degree$ in the direction of the positive y-axis. During one sweep, the sensor initially points at a fixed direction, and turns anti-clockwise in fixed angular intervals until it reaches a fixed maximum angle. The initial, final and interval angles are hardcoded in both `mapper.py` and `mapper.ino`. Note that both must be manually edited to match. This is described in [Servo motion.jpg](Servo%20motion.jpg). 

At each such angle, the ultrasonic sensor measures distance in millimeters (depicted in [Coordinates explanation.jpg](Coordinates%20explanation.jpg)). This can then be used to find Cartesian coordinates of the detected point relative to the sensor's position.

This process is repeated to create a point cloud of obstacle points.

### Program flow
1. When the `mapper.py` program is run, the user can choose to simply generate a visualization of existing data (stored in file called `data.txt`), or record new data, which is then appended to `data.txt`. In the former case, `numpy` and `matplotlib` are used to read the `data.txt` and generate a point cloud diagram. The program sequence in the latter case follows below.
2. Now, the user must push the measure pushbutton (on pin 8). This triggers a sweep. As the Arduino prints distance measurements to the serial port, the python program can read it using the `serial` library. Once all angles in this sweep are measured, the user is asked to state the sensor's position, relative to the origin of their global reference frame. 
3. Now, the user can move the sensor to a different position and measure again by pressing the pushbutton. Note that the sensor's **heading must not change** i.e. it must always point in the direction of the positive y-axis. Since the sensor's position at the time of measurement is recorded, measurements taken from different positions can then be fused together.
4. Once all measurements are completed, the user must press the END button (on pin 7). This ends measurement. The `mapper.py` program can move ahead and analyse the data now stored in `data.txt`. 
5. Once data analysis is complete, the resultant point cloud is displayed by matplotlib.

### Data Analysis
Each sweep, expressed in a line on `data.txt` consists of $n+1$ decimal numbers, $d_0, d_1, \cdots, d_n$ representing distance values. Here $n=\frac{\theta_{max}-\theta_{min}}{\theta_{interval}}$. This list is followed by two numbers denoting the sensor's position at the time of measurement $(x_{corr}, y_{corr})$ where $corr$ stands for _correction_.

Initially, any points outside of the sensor's measurement capabilities are discarded i.e. any measurements outside of $[20\text{mm}, 4000\text{mm}]$. 

First, the coordinates of a detected point is calculated in the sensor's reference frame.

$x_i = d_i \cos(\theta_i)$

$y_i = d_i \sin(\theta_i)$

$\text{where } \theta_i = \theta_{min} + i\cdot\theta_{interval}$


Next, this is translated to the global reference frame.

$x_{i, global} = x_i + x_{corr} = d_i \cos(\theta_i) + x_{corr}$

$y_{i, global} = y_i + y_{corr} = d_i \sin(\theta_i) + y_{corr} $

$\text{where } \theta_i = \theta_{min} + i\cdot\theta_{interval}$

Then, outliers are filtered out. Since the bounds of the field are known, any calculated points that fall out of these bounds can be discarded, since they may be a result of sensor noise or fall beyond the region of interest.

### Notes on Examples

In the following examples, different colours of points mean they were measured in different sweeps. In all these, the sensor is initially placed at (0,0) and moved about primarily on the x-axis at y=0.

**Figures 1-2**: Figure 1 shows a raw set of measurements, without excluding outliers. Figure 2 highlights how filtering out points outside bounds creates a more focused image.

**Figure 3**: The intersection of two walls was mapped.

**Figure 4**: A large number of sweeps were conducted with the sensor at different points. Many different angles allowed the sensor to 'see' three different walls, with one lying exactly hidden/covered by another.

**Figure 5**: A complicated scene was set for the sensor and it succeeded in creating a point cloud. In this example, the sensor was moved along both the x and y axes. A photograph of the real scene is also provided.